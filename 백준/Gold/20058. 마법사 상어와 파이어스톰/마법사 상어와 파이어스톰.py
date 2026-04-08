import sys
from collections import deque
input = sys.stdin.readline

def tornado(r, c, s):
    temp = [[0] * s for _ in range(s)]

    for i in range(s):
        for j in range(s):
            temp[j][s - 1 - i] = A[r + i][c + j]
    
    for i in range(s):
        for j in range(s):
            A[r + i][c + j] = temp[i][j]

def tornado_all(L):
    size = 2 ** L

    for r in range(0, N, size):
        for c in range(0, N, size):
            tornado(r, c, size)

def melt_ice():
    decrease = []

    for r in range(N):
        for c in range(N):
            if A[r][c] > 0:
                cnt = 0

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < N and 0 <= nc < N:
                        if A[nr][nc] > 0:
                            cnt += 1
                
                if cnt < 3:
                    decrease.append((r, c))

    for r, c in decrease:
        A[r][c] -= 1

def bfs(row, col):
    global count
    dq = deque()
    dq.append((row, col))
    visited[row][col] = True
    size = 1

    while dq:
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and A[nr][nc] > 0:
                    visited[nr][nc] = True
                    dq.append((nr, nc))
                    size += 1

    count = max(count, size) 

N, Q = map(int, input().split())
N = 2 ** N
A = [list(map(int, input().split())) for _ in range(N)]
L = list(map(int, input().split()))

visited = [[False] * N for _ in range(N)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
count = 0
result = 0

for i in L:
    if i > 0:
        tornado_all(i)

    melt_ice()

for i in range(N):
    for j in range(N):
        result += A[i][j]

for i in range(N):
    for j in range(N):
        if A[i][j] > 0 and not visited[i][j]:
            bfs(i, j)

print(result)
print(count)