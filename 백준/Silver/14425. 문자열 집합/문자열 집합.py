import sys

N, M = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().strip() for _ in range(N)]

cnt = 0

for _ in range(M):
    word = sys.stdin.readline().strip()

    if word in words:
        cnt += 1

print(cnt)