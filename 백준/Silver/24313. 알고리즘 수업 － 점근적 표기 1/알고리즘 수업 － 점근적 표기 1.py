import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

if a1 <= c and a1 * n0 + a0 <= c * n0:
    print(1)
else:
    print(0)