import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
orders = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
result = []

for p1, p2 in orders:
    graph[p1].append(p2)
    indegree[p2] += 1
    
heap = []

for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    current = heapq.heappop(heap)
    result.append(current)
    
    for next in graph[current]:
        indegree[next] -= 1
        
        if indegree[next] == 0:
            heapq.heappush(heap, next)
    
print(*result)