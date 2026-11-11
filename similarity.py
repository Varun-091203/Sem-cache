import math

def cosine_similarity(a, b):
    dot = 0
    for i in range(len(a)):
        dot = dot + a[i] *b[i]

    len_a = 0
    for x in a:
        len_a = len_a + x * x
    len_a = math.sqrt(len_a)

    len_b = 0
    for x in b:
        len_b = len_b + x * x
    len_b = math.sqrt(len_b)

    return dot / (len_a * len_b)

def find_most_similar(query, saved):
    best_key = None
    best_score = -1
    for key, vec in saved.items():
        score = cosine_similarity(query, vec)
        if score > best_score:
            best_score = score
            best_key = key
    return best_key, best_score