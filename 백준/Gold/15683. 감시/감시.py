import sys
from copy import deepcopy

def check(r, c):
    return r < 0 or r >= N or c < 0 or c >= M

def monitor(r, c, board, dir):
    for d in dir:
        nr = r
        nc = c

        while 1:
            nr += dr[d]
            nc += dc[d]

            if check(nr, nc) or board[nr][nc] == 6:
                break
            elif board[nr][nc] == 0:
                board[nr][nc] = -1

def dfs(depth, office):
    global min_value

    if depth == len(location):
        count = 0

        for i in range(N):
            count += office[i].count(0)
        min_value = min(min_value, count)

        return

    temp = deepcopy(office)
    num, r, c = location[depth]

    for i in direction[num]:
        monitor(r, c, temp, i)
        dfs(depth + 1, temp)
        
        temp = deepcopy(office)

if __name__ == "__main__":
    office = []
    cctv = [1, 2, 3, 4, 5]
    location = []
    direction = [[],
                [[0], [1], [2], [3]],
                [[0, 2], [1, 3]],
                [[0, 1], [1, 2], [2, 3], [3, 0]],
                [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
                [[0, 1, 2, 3]]]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    N, M = map(int, sys.stdin.readline().split())
    
    for _ in range(N):
        office.append(list(map(int, sys.stdin.readline().split())))

    for r in range(N):
        for c in range(M):
            if office[r][c] in cctv:
                location.append((office[r][c], r, c))
    
    min_value = int(1e9)

    dfs(0, office)

    print(min_value)