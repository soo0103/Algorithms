import sys
import heapq

INF = int(1e9)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

city = [[]for _ in range(N + 1)]
costs = [INF for _ in range(N + 1)]
heap = []

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    city[u].append((v, w))
        
start, end = map(int, sys.stdin.readline().split())

heapq.heappush(heap, (0, start))
costs[start] = 0

while heap:
    cost, node = heapq.heappop(heap)
    
    if costs[node] < cost:
        continue
    
    for next_node, next_cost in city[node]:
        if cost + next_cost < costs[next_node]:
            costs[next_node] = cost + next_cost
            heapq.heappush(heap, (cost + next_cost, next_node))

print(costs[end])