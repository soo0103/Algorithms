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

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    parent = [i for i in range(n + 1)]

    for i in range(m):
        op, a, b = map(int, sys.stdin.readline().split())

        if not op:
            union_parent(a, b)
        else:
            if find_parent(a) == find_parent(b):
                print("YES")
            else:
                print("NO")