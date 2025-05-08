import sys
import heapq

INF = int(1e9)

def dijkstra(start, end):
    distance = [INF] * (N + 1)
    heap = []

    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, current_node = heapq.heappop(heap)

        if distance[current_node] < weight:
            continue

        for weight, next_node in graph[current_node]:
            cost = distance[current_node] + weight
            
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(heap, (cost, next_node))

    return distance[end]

if __name__ == "__main__":
    N, M, X = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(N + 1)]
    result = [0] * (N + 1)

    for _ in range(M):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((w, v))

    for i in range(1, N + 1):
        result[i] = dijkstra(i, X) + dijkstra(X, i)
    
    print(max(result))