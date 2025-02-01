import sys

def DFS(arr, i, visited):
    global cnt
    visited[i] = True
    cnt += 1
    
    for j in range(len(arr[i])):
        if arr[i][j] == 1 and not visited[j]:
            DFS(arr, j, visited)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    arr = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        arr[a][b] = 1
        arr[b][a] = 1

    visited = [False for k in range(N + 1)]
    cnt = 0

    DFS(arr, 1, visited)

    print(cnt - 1)