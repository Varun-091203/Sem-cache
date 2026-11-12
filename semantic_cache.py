from lru import LRUCache
from embedder import Embedder
from similarity import find_most_similar
from llm_client import fake_llm

class SemanticCache:
    def __init__(self, capacity=100, threshold=0.85, ttl=None, llm=fake_llm):
        self.lru = LRUCache(capacity)
        self.embedder = Embedder()
        self.embeddings = {}
        self.threshold = threshold
        self.ttl = ttl
        self.llm = llm
        self.hits = 0
        self.misses = 0

    def _save(self, question, answer):
        self.lru.put(question, answer, self.ttl)
        self.embeddings[question] = self.embedder.embed(question)
        self._sync()

    def ask(self, question):
        answer = self.lru.get(question)
        if answer is not None:
            self.hits += 1
            return answer
        self._sync()
        if self.embeddings:
            query = self.embedder.embed(question)
            best, score = find_most_similar(query, self.embeddings)
            if score >= self.threshold:
                answer = self.lru.get(best)
                if answer is not None:
                    self.hits += 1
                    return answer
        answer = self.llm(question)
        self.misses += 1
        self._save(question, answer)
        return answer

    def _sync(self):
        for key in list(self.embeddings):
            if key not in self.lru.map:
                del self.embeddings[key]