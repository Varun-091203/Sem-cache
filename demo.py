import time
from semantic_cache import SemanticCache

sc = SemanticCache(threshold=0.8) 

questions = [
    "How do I reset my password?",            
    "How do I reset my password?",             
    "I forgot my password, what should I do?", 
    "What is the capital of France?",]

for q in questions:
    start = time.time()
    sc.ask(q)
    seconds = round(time.time() - start, 2)
    print(seconds, "s |", q)

print("hits:", sc.hits, "misses:", sc.misses)