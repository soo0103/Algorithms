import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    cnt = 0
    
    for i in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    
    print(cnt)