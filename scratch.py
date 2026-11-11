from embedder import Embedder
from similarity import find_most_similar

e = Embedder()
saved = {}
for q in ["How do I cancel my order?", "Whats is the captial of france", "How do I reset my password"]:
    saved[q] = e.embed(q)

new_question = "I forgot my password, what should I do?"
key, score = find_most_similar(e.embed(new_question), saved)
print(key)
print(round(score, 2))