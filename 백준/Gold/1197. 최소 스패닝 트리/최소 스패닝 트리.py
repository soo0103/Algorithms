import sys
sys.setrecursionlimit(10 ** 6)

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def has_cycle(a, b):
    return find_parent(a) == find_parent(b)

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    edges = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]

    edges.sort(key = lambda x: x[2])
    parent = [i for i in range(V + 1)]
    weight = 0

    for A, B, C in edges:
        if not has_cycle(A, B):
            union_parent(A, B)
            weight += C
    
    print(weight)