import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
INF = int(1e9)

graph = [[] for _ in range(V + 1)]
distance = [INF for _ in range(V + 1)]
heap = []

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

heapq.heappush(heap, (0, K))
distance[K] = 0

while heap:
    weight, node = heapq.heappop(heap)
    
    if distance[node] < weight:
        continue
    
    for i in graph[node]:
        if weight + i[1] < distance[i[0]]:
            distance[i[0]] = weight + i[1]
            heapq.heappush(heap, (weight + i[1], i[0]))
    
for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])