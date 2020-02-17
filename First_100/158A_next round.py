# 158A - next round
n, k = map(int, input().split())
scores_s = input().split()
scores = []
for i, score in enumerate(scores_s):
    scores.append(int(score))
k_th_place = scores[k - 1]
count = 0
for i, score in enumerate(scores):
    if score >= k_th_place and score > 0:
        count += 1
    else:
        break
print(count)