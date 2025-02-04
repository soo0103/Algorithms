import sys
from collections import deque

def crossProduct(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1

def ccw(x1, y1, x2, y2, x3, y3):
    value = crossProduct(x2 - x1, y2 - y1, x3 - x1, y3 - y1)

    if value > 0: 
        return 1
    elif value < 0: 
        return -1
    else:
        return 0

def isBetween(a, b, c):
    return min(a, b) <= c <= max(a, b)

def isIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
    d1 = ccw(x1, y1, x2, y2, x3, y3)
    d2 = ccw(x1, y1, x2, y2, x4, y4)
    d3 = ccw(x3, y3, x4, y4, x1, y1)
    d4 = ccw(x3, y3, x4, y4, x2, y2)

    if d1 * d2 < 0 and d3 * d4 < 0:
        return True
    if d1 == 0 and isBetween(x1, x2, x3) and isBetween(y1, y2, y3):
        return True
    if d2 == 0 and isBetween(x1, x2, x4) and isBetween(y1, y2, y4):
        return True
    if d3 == 0 and isBetween(x3, x4, x1) and isBetween(y3, y4, y1):
        return True
    if d4 == 0 and isBetween(x3, x4, x2) and isBetween(y3, y4, y2):
        return True
    return False

def bfs(n):
    dq = deque([n])
    size = 0

    while dq:
        line = dq.popleft()

        if visited[line]:
            continue

        visited[line] = True
        size += 1

        for next in graph[line]:
            if not visited[next]:
                dq.append(next)

    return size

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    graph = [[] for _ in range(N)]
    visited = [False] * N
    
    for i in range(N):
        for j in range(i + 1, N):
            if isIntersect(lines[i][0], lines[i][1], lines[i][2], lines[i][3], lines[j][0], lines[j][1], lines[j][2], lines[j][3]):
                graph[i].append(j)
                graph[j].append(i)

    cnt = 0
    size = 0

    for i in range(N):
        if not visited[i]:
            cnt += 1
            size = max(size, bfs(i))

    print(cnt)
    print(size)