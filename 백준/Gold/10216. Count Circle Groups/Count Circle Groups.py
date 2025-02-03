import sys

def dfs(i):
    visited[i] = True

    for j in range(N):
        if i != j and not visited[j]:
            if (coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2 <= (coordinates[i][2] + coordinates[j][2]) ** 2:
                dfs(j)

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        N = int(sys.stdin.readline())
        coordinates = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
        
        visited = [False] * N
        cnt = 0

        for i in range(N):
            if not visited[i]:
                cnt += 1
                dfs(i)

        print(cnt)