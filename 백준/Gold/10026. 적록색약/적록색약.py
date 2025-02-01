import sys
from collections import deque

def bfs():
    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]

            if 0 <= nx < N  and 0 <= ny < N:
                if pic[ny][nx] == pic[y][x] and not visited[ny][nx]:
                    dq.append((nx, ny))
                    visited[ny][nx] = True

if __name__ == "__main__":          
    N = int(sys.stdin.readline())
    pic = [list(sys.stdin.readline().strip()) for _ in range(N)]
    dq = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt1, cnt2 = 0, 0

    visited = [[False] * N for _ in range(N)]

    for j in range(N):
        for i in range(N):
            if not visited[j][i]:
                dq.append((i, j))
                visited[j][i] = True
                bfs()
                cnt1 += 1

    visited = [[False] * N for _ in range(N)]

    for j in range(N):
        for i in range(N):
            if pic[j][i] == 'G':
                pic[j][i] = 'R'
                
    for j in range(N):
        for i in range(N):
            if not visited[j][i]:
                dq.append((i, j))
                visited[j][i] = True
                bfs()
                cnt2 += 1

    print(cnt1, cnt2)