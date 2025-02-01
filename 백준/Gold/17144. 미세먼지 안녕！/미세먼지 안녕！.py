import sys
from collections import deque

def check(r, c):
    return r < 0 or r >= R or c < 0 or c >= C

def diffusion():
    while location:
        amount, r, c = location.popleft()
        cnt = 0
        dust = 0

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if check(nr, nc) or room[nr][nc] == -1:
                continue
            else:
                dust = amount // 5
                room[nr][nc] += dust
                cnt += 1

        room[r][c] -= dust * cnt
        
def clean(u, d):
    r, c = u, 0
    dir = 1
    temp = 0
    
    while 1:
        nr = r + dr[dir]
        nc = c + dc[dir]

        if nr == u and nc == 0:
            break
        elif check(nr, nc):
            dir = (dir + 3) % 4
            continue

        temp, room[nr][nc] = room[nr][nc], temp
        r = nr
        c = nc

    r, c = d, 0
    dir = 1
    temp = 0
    
    while 1:
        nr = r + dr[dir]
        nc = c + dc[dir]

        if nr == d and nc == 0:
            break
        elif check(nr, nc):
            dir = (dir + 1) % 4
            continue

        temp, room[nr][nc] = room[nr][nc], temp
        r = nr
        c = nc

if __name__ == "__main__":
    room = []
    location = deque()
    cleaner = []
    value = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    R, C, T = map(int, sys.stdin.readline().split())

    for _ in range(R):
        room.append(list(map(int, sys.stdin.readline().split())))

    for row in range(R):
        for col in range(C):
            if room[row][col] > 0:
                location.append((room[row][col], row, col))

            if room[row][col] == -1:
                cleaner.append(row)
                
    for _ in range(T):
        diffusion()
        clean(cleaner[0], cleaner[1])
        
        for row in range(R):
            for col in range(C):
                if room[row][col] > 0:
                    location.append((room[row][col], row, col))

    for row in range(R):
        for col in range(C):
            if room[row][col] > 0:
                value += room[row][col]

    print(value)