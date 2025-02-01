import sys

N = int(sys.stdin.readline())

X = []
Y = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())

    X.append(x)
    Y.append(y)

width = max(X) - min(X)
height = max(Y) - min(Y)

print(width * height)