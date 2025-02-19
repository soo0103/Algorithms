import sys

K = int(sys.stdin.readline())
D1, D2 = map(int, sys.stdin.readline().split())

H = K ** 2 - ((D2 - D1) / 2) ** 2

print(H)