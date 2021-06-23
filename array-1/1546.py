ct = int(input())
scores = input()
scores = list(map(int, scores.split()))[:ct]

m = max(scores)
new_scores = []
for i in scores:
    new_scores.append(i/m*100)

print(sum(new_scores)/len(new_scores))
