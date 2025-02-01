import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

P.sort()

time = 0
cnt = N

for i in P:
    time += i * cnt
    cnt -= 1

print(time)