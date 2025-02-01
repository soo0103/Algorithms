import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

visited = [[False] * M for _ in range(N)]

visited[r][c] = True
cnt = 1

while 1:
    flag = 0

    for i in range(4):
        d = (d + 3) % 4
        nr = r + dy[d]
        nc = c + dx[d]

        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            if not visited[nr][nc]:
                cnt += 1
                visited[nr][nc] = True
                r = nr
                c = nc
                flag = 1
                break
            
    if flag == 0:
        if room[r - dy[d]][c - dx[d]] == 1:
            print(cnt)
            break
        else:
            r -= dy[d]
            c -= dx[d]