import sys
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
    n = int(sys.stdin.readline())
    
    stars = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]
    
    edges = []
    parent = [i for i in range(n)]
    distance = 0
        
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = get_distance(stars[i], stars[j])
            edges.append((i, j, d))
            
    edges.sort(key=lambda x: x[2])
    
    for x, y, d in edges:
        if not has_cycle(x, y):
            union(x, y)
            distance += d
            
    print(round(distance, 2))