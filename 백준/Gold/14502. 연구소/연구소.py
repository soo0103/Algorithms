import sys
from copy import deepcopy
from collections import deque

def move():
    global safe
    cnt = 0
    virus = deepcopy(lab)
    
    for i in range(N):
        for j in range(M):
            if virus[i][j] == 2:
                dq.append((i, j))

    while dq:
        r, c = dq.popleft()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and virus[nr][nc] == 0:
                virus[nr][nc] = 2
                dq.append((nr, nc))
                    
    for i in range(N):
        for j in range(M):
            if virus[i][j] == 0:
                cnt += 1

    safe = max(cnt, safe)
        
def wall(cnt):
    if cnt == 3:
        move()
        return

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(cnt + 1)
                lab[i][j] = 0

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dq = deque()
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    safe = 0

    wall(0)
    
    print(safe)