import sys

N = int(sys.stdin.readline())

scores = [int(sys.stdin.readline()) for _ in range(N)]

cnt = 0
now = scores[-1]

for i in range(N - 2, -1, -1):
    if scores[i] >= now:
        cnt += scores[i] - now + 1
        now -= 1
    else:
        now = scores[i]

print(cnt)