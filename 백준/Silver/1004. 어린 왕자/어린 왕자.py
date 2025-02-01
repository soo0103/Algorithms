import sys

T = int(sys.stdin.readline())

for _ in range(T):
    cnt = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    
    for _ in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        d1 = ((x1 - cx) ** 2 + (y1 - cy) ** 2) ** 0.5
        d2 = ((x2 - cx) ** 2 + (y2 - cy) ** 2) ** 0.5

        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
            cnt += 1
    
    print(cnt)