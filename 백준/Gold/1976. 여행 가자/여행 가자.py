import sys

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
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())

    adjacency_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    plan = list(map(int, sys.stdin.readline().split()))

    parent = [i for i in range(N + 1)]

    for i in range(N):
        for j in range(N):
            if i != j and adjacency_matrix[i][j] == 1:
                union(i + 1, j + 1)

    flag = True

    for i in range(len(plan) - 1):
        if parent[plan[i]] != parent[plan[i + 1]]:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")