import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, c):
    global flag
    
    if color[x] == -1:
        color[x] = c
    
    for nxt in graph[x]:
        if color[nxt] != -1:
            if color[nxt] == c:
                flag = False
                return
        else:
            dfs(nxt, (c + 1) % 2)

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        V, E = map(int, sys.stdin.readline().split())
        
        graph = [[] for _ in range(V + 1)]
        color = [-1] * (V + 1)
        flag = True
        
        for _ in range(E):
            u, v = map(int, sys.stdin.readline().split())
            graph[u].append(v)
            graph[v].append(u)

        for i in range(1, V + 1):
            if color[i] == -1:
                dfs(i, 0)
        
        if flag:
            print('YES')
        else:
            print('NO')