import sys
from collections import deque

def bfs(row, col, shark):
    global time
    global cnt
    global size
    
    size = shark
    dq = deque()
    dq.append((row, col))
    visited = [[False for _ in range(N)] for _ in range(N)]
    distance = [[0 for _ in range(N)] for _ in range(N)]
    
    fish = []
    
    while dq:
        r, c = dq.popleft()
        visited[r][c] = True

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if size >= space[nr][nc]:
                    visited[nr][nc] = True
                    dq.append((nr, nc))
                    distance[nr][nc] = distance[r][c] + 1
                    
                    if 1 <= space[nr][nc] < size:
                        fish.append((nr, nc, distance[nr][nc]))

    if fish:            
        fish.sort(key = lambda x : (x[2], x[0], x[1]))
        return fish[0]

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    space = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    cnt = 0
    time = 0
    size = 2
    now_r = 0
    now_c = 0

    for _ in range(N):
        space.append(list(map(int, sys.stdin.readline().split())))

    for r in range(N):
        for c in range(N):
            if space[r][c] == 9:
                bfs(r, c, 2)
                now_r = r
                now_c = c
                space[r][c] = 0
                
    while True:
        result = bfs(now_r, now_c, size)
        if result is None:
            break
        
        r, c, t = result
        cnt += 1

        if cnt == size:
            size += 1
            cnt = 0
        time += t
        
        space[r][c] = 0
        now_r = r
        now_c = c

    print(time)