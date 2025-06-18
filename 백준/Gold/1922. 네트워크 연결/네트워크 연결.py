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
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    costs = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    costs.sort(key = lambda x: x[2])
    parent = [i for i in range(N + 1)]
    weight = 0

    for a, b, c in costs:
        if not has_cycle(a, b):
            union_parent(a, b)
            weight += c
    
    print(weight)