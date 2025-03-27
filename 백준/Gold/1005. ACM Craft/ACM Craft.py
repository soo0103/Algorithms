import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    D = [0] + list(map(int, sys.stdin.readline().split()))
    orders = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
    W = int(sys.stdin.readline())

    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    time = [0] * (N + 1)

    for X, Y in orders:
        graph[X].append(Y)
        indegree[Y] += 1

    dq = deque()

    for i in range(N + 1):
        if indegree[i] == 0:
            dq.append(i)
            time[i] = D[i]

    while dq:
        current = dq.popleft()

        for next in graph[current]:
            indegree[next] -= 1
            time[next] = max(time[next], time[current] + D[next])

            if indegree[next] == 0:
                dq.append(next)

    print(time[W])