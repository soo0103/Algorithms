import sys

A = int(sys.stdin.readline())
op = sys.stdin.readline().strip()
B = int(sys.stdin.readline())

if op == '*':
    print(A * B)
else:
    print(A + B)