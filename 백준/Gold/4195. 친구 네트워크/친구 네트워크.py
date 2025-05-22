import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
        count[a] += count[b]

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        F = int(sys.stdin.readline())

        parent = {}
        count = {}

        for _ in range(F):
            f1, f2 = sys.stdin.readline().split()
            
            if f1 not in parent:
                parent[f1] = f1
                count[f1] = 1
            if f2 not in parent:
                parent[f2] = f2
                count[f2] = 1
            
            union(f1, f2)

            print(count[parent[f1]])