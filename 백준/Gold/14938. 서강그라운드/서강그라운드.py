import sys
import heapq

INF = int(1e9)

def dijkstra(start):
    length[start] = 0
    
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        current_length, current_region = heapq.heappop(heap)

        if length[current_region] < current_length:
            continue

        for next_length, next_region in graph[current_region]:
            total_length = current_length + next_length

            if total_length < length[next_region]:
                length[next_region] = total_length
                heapq.heappush(heap, (total_length, next_region))

if __name__ == "__main__":
    n, m, r = map(int, sys.stdin.readline().split())
    t = list(map(int, sys.stdin.readline().split()))

    total_items = 0
    graph = [[] for _ in range(n + 1)]

    for _ in range(r):
        a, b, l = map(int, sys.stdin.readline().split())
        graph[a].append((l, b))
        graph[b].append((l, a))

    for i in range(1, n + 1):
        items = 0
        length = [INF] * (n + 1)

        dijkstra(i)

        for j in range(1, n + 1):
            if length[j] <= m:
                items += t[j - 1]

        if total_items < items:
            total_items = items

    print(total_items)