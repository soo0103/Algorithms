import sys
import heapq

INF = int(1e9)

def dijkstra(start, end):
    heap = []
    distance = [INF] * (N + 1)
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, node = heapq.heappop(heap)
        if dist <= distance[node]:
            for w, n in graph[node]:
                cost = distance[node] + w
                if cost < distance[n]:
                    distance[n] = cost
                    heapq.heappush(heap, (distance[n], n))
    
    return distance[end]

if __name__ == "__main__":
    N, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    v1, v2 = map(int, sys.stdin.readline().split())

    p1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
    p2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

    result = min(p1, p2)
 
    if result >= INF:
        print(-1)
    else:
        print(result)