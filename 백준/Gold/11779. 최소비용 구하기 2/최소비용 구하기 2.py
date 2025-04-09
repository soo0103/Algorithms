import sys
import heapq

INF = int(1e9)

def dijkstra(start):
    heapq.heappush(heap, (0, start))
    costs[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)
        
        if costs[node] < cost:
            continue
        
        for next_node, next_cost in city[node]:
            if cost + next_cost < costs[next_node]:
                prev[next_node] = node
                costs[next_node] = cost + next_cost
                heapq.heappush(heap, (cost + next_cost, next_node))

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())

    city = [[] for _ in range(n + 1)]
    costs = [INF for _ in range(n + 1)]
    heap = []

    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        city[u].append((v, w))

    start, end = map(int, sys.stdin.readline().split())

    prev = [0] * (n + 1)
    path = [end]

    dijkstra(start)

    current = end

    while current != start:
        path.append(prev[current])
        current = prev[current]

    print(costs[end])
    print(len(path))
    print(*reversed(path))