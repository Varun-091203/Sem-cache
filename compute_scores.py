import csv                                          
from datasets import load_dataset
from embedder import Embedder
from similarity import cosine_similarity

data = load_dataset("nyu-mll/glue", "qqp", split="validation")
data = data.shuffle(seed=42).select(range(1000))    

e = Embedder()                                      
rows = []                                           
for item in data:
    a = e.embed(item["question1"])                  
    b = e.embed(item["question2"])                  
    rows.append((cosine_similarity(a, b), item["label"]))   
    if len(rows) % 100 == 0:                        
        print("done", len(rows))

with open("scores.csv", "w", newline="") as f:      
    writer = csv.writer(f)
    writer.writerow(["score", "label"])             
    writer.writerows(rows)                          
print("saved", len(rows))