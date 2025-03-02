import sys

A, B = map(int, sys.stdin.readline().split())

result = A * B

while B:
    A %= B
    A, B = B, A

print(result // A)