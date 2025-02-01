import sys

import sys
sys.setrecursionlimit(10 ** 6)

def dfs(start):
    for node in graph[start]:
        if parent[node] == 0:
            parent[node] = start
            dfs(node)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    
    parent = [0 for _ in range(N + 1)]
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(N - 1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
            
    dfs(1)

    for i in parent[2:]:
        print(i)