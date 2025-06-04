import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
required = [[0] * (N + 1) for _ in range(N + 1)]
dq = deque()

for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().split())
    graph[Y].append((X, K))
    indegree[X] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        dq.append(i)

while dq:
    current = dq.popleft()

    for nxt, next_required in graph[current]:
        if sum(required[current]) == 0:
            required[nxt][current] += next_required
        else:
            for i in range(1, N + 1):
                required[nxt][i] += required[current][i] * next_required

        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            dq.append(nxt)

for req in enumerate(required[N]):
    if req[1] > 0:
        print(*req)