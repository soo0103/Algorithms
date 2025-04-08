import sys

N = int(sys.stdin.readline())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

maps = [['0'] * N for _ in range(N)]

dr = [1, 1, 1, 0, 0, -1, -1, -1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for r in range(N):
    for c in range(N):
        if board[r][c].isdigit():
            maps[r][c] = '*'
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < N and 0 <= nc < N:
                    if maps[nr][nc] != '*':
                        if maps[nr][nc].isdigit():
                            value = int(maps[nr][nc]) + int(board[r][c])
                            maps[nr][nc] = 'M' if value >= 10 else str(value)

for i in maps:
    print(*i, sep='')