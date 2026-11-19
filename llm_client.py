import time
from google import genai

def fake_llm(question):
    time.sleep(1)
    return "Answer to: " + question

def real_llm(question):
    client = genai.Client()
    response = client.models.generate_content(model="gemini-3.5-flash-lite",contents=question,)
    return response.text