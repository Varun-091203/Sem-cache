import time
from semantic_cache import SemanticCache

def quick_llm(question):
    return "answer"

sc = SemanticCache(llm=quick_llm)
for i in range(100):
    sc.ask("saved question number" + str(i))

start = time.time()
for i in range(20):
    sc.ask("a brand new question" + str(i) + " about something else")
total = time.time() - start

print(round(1000 * total / 20), "milliseconds per request")   # average time, in milliseconds