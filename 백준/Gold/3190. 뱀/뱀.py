import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

board = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    board[r][c] = -1
    
L = int(sys.stdin.readline())
directions = deque([list(sys.stdin.readline().split()) for _ in range(L)])

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dq = deque([(1, 1)])
r, c = 1, 1
i = 0
sec = 0

while 1:
    nr = r + dr[i]
    nc = c + dc[i]
    sec += 1

    if nr < 1 or nr > N or nc < 1 or nc > N or (nr, nc) in dq:
        break

    if board[nr][nc] == -1:
        dq.append((nr, nc))
        board[nr][nc] = 0
    else:
        dq.popleft()
        dq.append((nr, nc))

    if directions and int(directions[0][0]) == sec:
        if directions[0][1] == 'L':
            i = (i + 3) % 4
        else:
            i = (i + 1) % 4
        
        directions.popleft()

    r, c = nr, nc

print(sec)