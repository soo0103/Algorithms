import sys
from collections import deque

INF = int(1e9)

def bfs(x):
    dq = deque()
    dq.append(x)

    while dq:
        current = dq.popleft()
        
        for nxt in graph[current]:
            if distance[nxt] == INF:
                distance[nxt] = distance[current] + 1
                dq.append(nxt)

if __name__ == "__main__":
    N, M, K, X = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        graph[A].append(B)

    distance = [INF] * (N + 1)
    distance[X] = 0

    bfs(X)

    flag = False

    for i in range(1, N + 1):
        if distance[i] == K:
            print(i)
            flag = True

    if not flag:
        print(-1)