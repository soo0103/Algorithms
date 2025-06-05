import sys

def is_intersect(r1, r2):
    if r2[0] > r1[0] and r1[2] > r2[2] and r2[1] > r1[1] and r1[3] > r2[3]:
        return False
    if r1[0] > r2[0] and r2[2] > r1[2] and r1[1] > r2[1] and r2[3] > r1[3]:
        return False
    if r2[0] > r1[2] or r1[0] > r2[2] or r2[1] > r1[3] or r1[1] > r2[3]:
        return False
    return True

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
    
    rectangles = []
    flag = False

    for i in range(N):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        
        if (x1 == 0 or x2 == 0) and y1 <= 0 <= y2:
            flag = True
        if (y1 == 0 or y2 == 0) and x1 <= 0 <= x2:
            flag = True

        rectangles.append((x1, y1, x2, y2))

    parent = [i for i in range(N)]

    for i in range(N - 1):
        for j in range(i + 1, N):
            if is_intersect(rectangles[i], rectangles[j]):
                union(i, j)

    for i in range(N):
        parent[i] = find(i)

    cnt = len(set(parent))
    
    if flag:
        cnt -= 1

    print(cnt)