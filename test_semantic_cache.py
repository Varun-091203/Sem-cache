from semantic_cache import SemanticCache

def quick_llm(question): 
    return "answer"

def test_exact_repeat_is_a_hit():
    sc = SemanticCache(llm=quick_llm)
    sc.ask("How do I reset my password?")
    sc.ask("How do I reset my password?")
    assert sc.hits == 1
    assert sc.misses == 1

def test_similar_meaning_is_a_hit():
    sc = SemanticCache(threshold=0.8, llm=quick_llm)
    sc.ask("How do I reset my password?")
    sc.ask("I forgot my password, what should I do?")
    assert sc.hits == 1
    assert sc.misses == 1

def test_unrelated_question_is_a_miss():
    sc = SemanticCache(threshold=0.8, llm=quick_llm)
    sc.ask("How do I reset my password?")
    sc.ask("What is the capital of France?")
    assert sc.hits == 0
    assert sc.misses == 2

def test_embeddings_stay_in_sync_with_cache():
    sc = SemanticCache(capacity=1, llm=quick_llm)
    sc.ask("How do I reset my password?")
    sc.ask("What is the capital of France?")
    assert len(sc.embeddings) == len(sc.lru.map)