import sys

A, B = map(int, sys.stdin.readline().split())

M = (B - A) / 400
P = 1 / (1 + 10 ** M)

print(P)