import sys
from collections import deque

def DFS(arr, i, visited):
    visited[i] = True
    print(i, end=' ')

    for j in range(len(arr[i])):
        if arr[i][j] == 1 and not visited[j]:
            DFS(arr, j, visited)
            
def BFS(arr, i, visited):
    dq = deque()
    dq.append(i)

    while dq:
        vertex = dq.popleft()

        if not visited[vertex]:
            print(vertex, end = ' ')
            visited[vertex] = True

            for j in range(len(arr[vertex])):
                if arr[vertex][j] == 1 and not visited[j]:
                    dq.append(j)

if __name__ == "__main__":
    N, M, V = map(int, sys.stdin.readline().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        arr[a][b] = 1
        arr[b][a] = 1

    visited = [False for k in range(N + 1)]

    DFS(arr, V, visited)

    visited = [False for k in range(N + 1)]
    print()
    
    BFS(arr, V, visited)