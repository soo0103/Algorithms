import sys
from collections import deque

def BFS():
    global cnt

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                dq.append((nx, ny))
    
    return
 
if __name__ == "__main__":
    box = []
    cnt = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dq = deque()

    M, N = map(int, sys.stdin.readline().split())

    for _ in range(N):
        box.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                dq.append((j, i))
    
    BFS()

    for l in box:
        for m in l:
            if m == 0:
                print(-1)
                exit(0)
        cnt = max(cnt, max(l))

    print(cnt - 1)