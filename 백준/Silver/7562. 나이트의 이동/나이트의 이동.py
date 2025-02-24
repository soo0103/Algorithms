import sys
from collections import deque

def bfs(current):
    cnt = 0
    dq = deque()
    dq.append((current, 0))

    while dq:
        (r, c), cnt = dq.popleft()

        if (r, c) == goal:
            return cnt

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < I and 0 <= nc < I and not visited[nr][nc]:
                visited[nr][nc] = True
                dq.append(((nr, nc), cnt + 1))

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        I = int(sys.stdin.readline())

        current = tuple(map(int, sys.stdin.readline().split()))
        goal = tuple(map(int, sys.stdin.readline().split()))

        chess = [[0] * I for _ in range(I)]
        visited = [[False] * I for _ in range(I)]
        dr = [-1, -2, -2, -1, 1, 2, 2, 1]
        dc = [-2, -1, 1, 2, -2, -1, 1, 2]

        visited[current[0]][current[1]] = True
        cnt = bfs(current)

        print(cnt)