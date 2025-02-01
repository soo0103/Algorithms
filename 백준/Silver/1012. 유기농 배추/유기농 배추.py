import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i]
    
        if 0 <= nx < N and 0 <= ny < M: 
            if cabbage[nx][ny] == 1: 
                cabbage[nx][ny] = -1 
                dfs(nx, ny)

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T): 
        M, N, K = map(int, sys.stdin.readline().split())
        cabbage = [[0] * M for _ in range(N)]
        cnt = 0
        dx = [1, -1, 0, 0] 
        dy = [0, 0, 1, -1]

        for i in range(K):
            m, n = map(int, sys.stdin.readline().split())
            cabbage[n][m] = 1

        for i in range(N):
            for j in range(M):
                if cabbage[i][j] > 0:
                    dfs(i, j)
                    cnt += 1 

        print(cnt)