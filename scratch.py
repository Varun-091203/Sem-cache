from semantic_cache import SemanticCache

sc = SemanticCache(capacity=1)                   
sc.ask("How do I reset my password?")            
sc.ask("What is the capital of France?")         
print(len(sc.lru.map))                           
print(len(sc.embeddings))                        