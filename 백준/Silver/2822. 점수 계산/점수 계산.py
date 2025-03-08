import sys

scores = [int(sys.stdin.readline()) for _ in range(8)]
sorted_scores = sorted(scores, reverse=True)

total = sum(sorted_scores[:5])

idx = [scores.index(score) + 1 for score in sorted_scores]

print(total)
print(*sorted(idx[:5]))