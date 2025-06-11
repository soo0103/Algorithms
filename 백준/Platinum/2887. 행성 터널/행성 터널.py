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

def has_cycle(a, b):
    return find(a) == find(b)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    
    xs = []
    ys = []
    zs = []
    
    for i in range(N):
        x, y, z = map(int, sys.stdin.readline().split())
        
        xs.append((x, i))
        ys.append((y, i))
        zs.append((z, i))
        
    xs.sort()
    ys.sort()
    zs.sort()
    
    parent = [i for i in range(N + 1)]
    
    edges = []
    
    for current_list in xs, ys, zs:
        for i in range(1, N):
            c1, a = current_list[i - 1]
            c2, b = current_list[i]
            heapq.heappush(edges, (abs(c1 - c2), a, b))
    
    cost = 0
    
    while edges:
        c, a, b = heapq.heappop(edges)
        
        if not has_cycle(a, b):
            union(a, b)
            cost += c
    
    print(cost)