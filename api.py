import time
import threading 
from fastapi import FastAPI
from fastapi.responses import FileResponse
from semantic_cache import SemanticCache

app = FastAPI()
cache = SemanticCache(threshold=0.8)
lock = threading.Lock()

@app.get("/hello")
def hello():
    return{"message": "Hello from SemCache"}

@app.get("/ask")
def ask(question: str):
    start = time.time()
    with lock:
         before = cache.hits
         answer = cache.ask(question)
         from_cache = cache.hits > before
    seconds = round(time.time() - start, 2)
    return {"question": question, "answer": answer, "seconds": seconds, "from_cache": from_cache}

@app.get("/stats")
def stats():
    total = cache.hits + cache.misses
    if total == 0:
        hit_rate = 0
    else:
        hit_rate = round(cache.hits / total, 2)
    return {"hits": cache.hits, "misses": cache.misses, "hit_rate": hit_rate}

@app.get("/")
def home():
    return FileResponse("index.html")