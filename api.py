import time
import threading 
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from semantic_cache import SemanticCache
from llm_client import real_llm

app = FastAPI()
DEMO_THRESHOLD = 0.8                           
cache = SemanticCache(threshold=DEMO_THRESHOLD, llm=real_llm)
lock = threading.Lock()

@app.get("/hello")
def hello():
    return{"message": "Hello from SemCache"}

@app.get("/ask")
def ask(question: str):
    start = time.time()
    with lock:
        before = cache.hits
        try:
            answer = cache.ask(question)
        except Exception as error:
            print("AI error:", error)
            raise HTTPException(
                status_code=503,
                detail="The AI service is not available right now. Try again in a minute.",
            )
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