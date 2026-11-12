import csv
import matplotlib.pyplot as plt

scores =[]
labels =[]
with open("scores.csv") as f:
    for row in csv.DictReader(f):
        scores.append(float(row["score"]))
        labels.append(int(row["label"]))
duplicates = sum(labels)

thresholds = []
caught_list = []
wrong_list = []
for i in range(50, 100):
    t = i / 100
    caught = 0
    wrong = 0
    for s, l in zip(scores, labels):
        if s >= t:
            if l == 1:
                caught = caught + 1
            else:
                wrong = wrong + 1
    hits = caught + wrong
    thresholds.append(t)
    caught_list.append(100 * caught / duplicates)
    wrong_list.append(100 * wrong / hits if hits > 0 else 0)

plt.plot(thresholds, caught_list, label ="Repeast caught (%)")
plt.plot(thresholds, wrong_list, label="Wrong among hits (%)")
plt.xlabel("Similarity threshold")
plt.ylabel("Percent")
plt.title("Choosing the threshold on 1000 Quora questions pairs")
plt.legend()
plt.savefig("threshold_chart.png")
print("saved threshold_chart.png")