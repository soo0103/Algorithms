import sys

N = int(sys.stdin.readline())

for i in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    
    if distance == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if distance == r1 + r2 or distance == abs(r1 - r2):
            print(1)
        elif r1 + r2 > distance and abs(r1 - r2) < distance:
            print(2)
        else:
            print(0)