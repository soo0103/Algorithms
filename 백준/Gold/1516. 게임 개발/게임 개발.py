import sys
from collections import deque

N = int(sys.stdin.readline())

times = [0] * (N + 1)
result = [0] * (N + 1)
buildings = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
dq = deque()

for i in range(1, N + 1):
    info = list(map(int, sys.stdin.readline().split()))[:-1]
    
    times[i] = info[0]

    for j in info[1:]:
        buildings[j].append(i)
        indegree[i] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        dq.append(i)
        result[i] = times[i]

while dq:
    current = dq.popleft()

    for nxt in buildings[current]:
        indegree[nxt] -= 1
        result[nxt] = max(result[current] + times[nxt], result[nxt])

        if indegree[nxt] == 0:
            dq.append(nxt)

print(*result[1:], sep='\n')