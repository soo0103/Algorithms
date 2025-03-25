import sys

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
    n, m = map(int, sys.stdin.readline().split())
    points = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

    parent = [i for i in range(n)]

    idx = 0

    for i in range(m):
        if has_cycle(points[i][0], points[i][1]):
            idx = i + 1
            break
        else:
            union_parent(points[i][0], points[i][1])

    print(idx)