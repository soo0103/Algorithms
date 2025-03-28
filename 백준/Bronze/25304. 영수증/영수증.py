import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
products = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

value = 0

for i in range(N):
    value += products[i][0] * products[i][1]

if value == X:
    print("Yes")
else:
    print("No")