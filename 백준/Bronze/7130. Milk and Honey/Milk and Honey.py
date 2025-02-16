import sys

M, H = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

happiness = 0

for _ in range(N):
    C, B = map(int, sys.stdin.readline().split())

    happiness += max(C * M, B * H)

print(happiness)