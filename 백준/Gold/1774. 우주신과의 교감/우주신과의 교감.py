import sys
import heapq
sys.setrecursionlimit(10 ** 6)

def get_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

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

def has_cycle(a, b):
    return find(a) == find(b)

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    gods = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    edges = []
    parent = [i for i in range(N + 1)]
    distance = 0

    for _ in range(M):
        X, Y = map(int, sys.stdin.readline().split())
        union(X, Y)
    
    for i in range(N - 1):
        for j in range(i + 1, N):
            d = get_distance(gods[i], gods[j])
            heapq.heappush(edges, (d, i + 1, j + 1))
    
    while edges:
        d, X, Y = heapq.heappop(edges)

        if not has_cycle(X, Y):
            union(X, Y)
            distance += d
            
    print("{:.2f}".format(distance))