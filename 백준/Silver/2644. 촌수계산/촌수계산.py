import sys

def DFS(p, cnt):
    global flag
    visited[p] = True

    if p == b:
        flag = True
        result.append(cnt)
        return
    else:
        for s in arr[p]:
            if not visited[s]:
                DFS(s, cnt + 1)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    a, b = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())

    arr = [[] for _ in range(n + 1)]
    result = []
    
    for i in range(m):
        x, y = map(int, sys.stdin.readline().split())
        arr[x].append(y)
        arr[y].append(x)

    visited = [False for _ in range(n + 1)]
    flag = False
    
    DFS(a, 0)
    
    if flag:
        print(result[0])
    else:
        print(-1)