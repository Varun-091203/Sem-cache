import csv

scores = []
labels = []
with open("scores.csv") as f:
    for row in csv.DictReader(f):
        scores.append(float(row["score"]))
        labels.append(int(row["label"]))

duplicates = sum(labels)
print("pairs:", len(labels), "duplicates:", duplicates)

for t in [0.9, 0.93, 0.95, 0.96, 0.97, 0.98, 0.99]:
    caught = 0
    wrong = 0
    for s, l in zip(scores, labels):
        if s >= t:
            if l == 1:
                caught = caught + 1
            else:
                wrong = wrong + 1
    hits = caught + wrong
    caught_pct = round(100 * caught / duplicates)
    wrong_pct = round(100 * wrong / hits) if hits > 0 else 0
    print(t, "| repeats caught:", caught_pct, "% | wrong among hits:", wrong_pct, "%")
