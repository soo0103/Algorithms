import sys

T = int(sys.stdin.readline())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(T):
    cmd = list(map(str, sys.stdin.readline().strip()))
    cnt = 0
    x1, y1, x2, y2 = 0, 0, 0, 0
    x, y = 0, 0

    for j in cmd:
        if j == "F":
            x += dx[cnt]
            y += dy[cnt]
        elif j == "B":
            x -= dx[cnt]
            y -= dy[cnt]
        elif j == "L":
            if cnt == 3:
                cnt = 0
            else:
                cnt += 1
        elif j == "R":
            if cnt == 0:
                cnt = 3
            else:
                cnt -= 1

        x1 = min(x1, x)
        y1 = min(y1, y)
        x2 = max(x2, x)
        y2 = max(y2, y)
        
    print(abs(x2 - x1) * abs(y2 - y1))