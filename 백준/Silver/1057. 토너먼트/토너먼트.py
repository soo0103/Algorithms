import sys

N, jm, hs = map(int, sys.stdin.readline().split())

cnt = 0

while jm != hs:
    jm -= jm // 2
    hs -= hs // 2
    cnt += 1

print(cnt)