import sys

N = int(sys.stdin.readline())
coordinate = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

coordinate.sort(key = lambda x : (x[1], x[0]))

for x, y in coordinate:
    print(x, y)