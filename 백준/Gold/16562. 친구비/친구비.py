import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if A[a] < A[b]:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    N, M, k = map(int, sys.stdin.readline().split())
    A = [0] + list(map(int, sys.stdin.readline().split()))
    
    parent = [i for i in range(N + 1)]

    for _ in range(M):
        v, w = map(int, sys.stdin.readline().split())
        union(v, w)
        
    friends = set()
    cost = 0
    
    for i in range(1, N + 1):
        if find(i) not in friends:
            cost += A[parent[i]]
            friends.add(parent[i])
            
    if cost > k:
        print("Oh no")
    else:
        print(cost)