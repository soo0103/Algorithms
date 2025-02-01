import sys
from collections import deque

def bfs(row, col, visited):
    dq = deque()
    dq.append((row, col))
    visited[row][col] = True
    union = [(row, col)]
    total = country[row][col]

    while dq:
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if L <= abs(country[r][c] - country[nr][nc]) <= R:
                    visited[nr][nc] = True
                    dq.append((nr, nc))
                    union.append((nr, nc))
                    total += country[nr][nc]

    if len(union) > 1:
        new_population = total // len(union)

        for r, c in union:
            country[r][c] = new_population

        return True
    
    return False

if __name__ == "__main__":
    N, L, R = map(int, sys.stdin.readline().split())
    
    days = 0
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    country = []

    for _ in range(N):
        country.append(list(map(int, sys.stdin.readline().split())))

    while 1:
        visited = [[False] * N for _ in range(N)]
        moved = False

        for r in range(N):
            for c in range(N):
                if not visited[r][c]:
                    if bfs(r, c, visited):
                        moved = True

        if not moved:
            break

        days += 1

    print(days)