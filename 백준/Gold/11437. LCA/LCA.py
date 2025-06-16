import sys
from collections import deque

def get_depth(current, d):
    dq = deque()
    dq.append((current, d))
    
    while dq:
        now, d = dq.popleft()
        
        counted[now] = True
        depth[now] = d
    
        for nxt in graph[now]:
            if counted[nxt]:
                continue
            parent[nxt] = now
            dq.append((nxt, d + 1))

def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
            
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    parent = [0] * (N + 1)
    depth = [0] * (N + 1)
    counted = [False] * (N + 1)
    graph = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        
    get_depth(1, 0)

    M = int(sys.stdin.readline())
    
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        print(lca(a, b))