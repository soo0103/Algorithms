import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
orders = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for A, B in orders:
    graph[A].append(B)
    indegree[B] += 1

dq = deque()
result = []

for i in range(N + 1):
    if indegree[i] == 0:
        dq.append(i)

while dq:
    current = dq.popleft()
    result.append(current)

    for next in graph[current]:
        indegree[next] -= 1
        if indegree[next] == 0:
            dq.append(next)

print(*result[1:])