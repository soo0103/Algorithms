import sys

def backtracking(node, cnt):
    global result

    if cnt == 4:
        result = 1
        return
    
    visited[node] = True

    for friend in graph[node]:
        if not visited[friend]:
            backtracking(friend, cnt + 1)
    
    visited[node] = False

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    
    graph = [[] for _ in range(N)]
    result = 0

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(N):
        visited = [False] * N

        backtracking(i, 0)

        if result:
            print(1)
            break

    if not result:
        print(0)