import sys
from collections import deque

def BFS():
    global cnt
    dq = deque()
    dq.append((0, 0))

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and maze[ny][nx] == 1:
                if visited[ny][nx] == False:
                    visited[ny][nx] = True
                    dq.append((nx, ny))
                    maze[ny][nx] = maze[y][x] + 1
    
    return
 
if __name__ == "__main__":
    maze = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 0

    N, M = map(int, sys.stdin.readline().split())
    visited = [[False] * M for _ in range(N)]

    for _ in range(N):
        maze.append(list(map(int, input())))

    BFS()
    
    print(maze[N - 1][M - 1])