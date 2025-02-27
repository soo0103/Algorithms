import sys

N, M = map(int, sys.stdin.readline().split())

fish = [list(map(int, str(sys.stdin.readline().strip()))) for _ in range(N)]

for f in fish:
    print(*f[::-1], sep = '')