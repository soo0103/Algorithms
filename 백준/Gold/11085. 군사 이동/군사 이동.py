import sys
import heapq

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    p, w = map(int, sys.stdin.readline().split())
    c, v = map(int, sys.stdin.readline().split())

    graph = []
    parent = [i for i in range(p + 1)]

    for _ in range(w):
        start, end, width = map(int, sys.stdin.readline().split())
        heapq.heappush(graph, (-width, start, end))

    min_width = 0

    while graph:
        w, s, e = heapq.heappop(graph)
        union(s, e)

        if find(c) == find(v):
            min_width = -w
            break
    
    print(min_width)