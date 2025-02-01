import sys

N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
avg = (sum(score) / max(score) * 100) / len(score)

print(avg)