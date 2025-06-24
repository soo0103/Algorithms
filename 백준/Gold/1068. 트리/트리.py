import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, rmv):
    global cnt
    if x == rmv:
        return
    
    if not graph[x] or (len(graph[x]) == 1 and graph[x][0] == rmv):
        cnt += 1
        return
    else:
        for nxt in graph[x]:
            dfs(nxt, rmv)
        
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    tree = list(map(int, sys.stdin.readline().split()))
    remove = int(sys.stdin.readline())

    graph = [[] for _ in range(N)]
    cnt = 0

    for i in range(N):
        if tree[i] != -1:
            graph[tree[i]].append(i)

    for i in range(N):
        if tree[i] == -1:
            if i == remove:
                break
            else:
                dfs(i, remove)
    
    print(cnt)