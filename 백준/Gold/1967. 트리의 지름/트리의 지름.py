import sys
sys.setrecursionlimit(10 ** 6)

def dfs(start, cost):
    global max_distance
    global max_distance_node
    current_node = start

    if cost > max_distance:
        max_distance = cost
        max_distance_node = start

    for next_node, weight in graph[current_node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, cost + weight)

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    max_distance = 0
    max_distance_node = 0

    for _ in range(n - 1):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    visited[1] = True
    dfs(1, 0)

    visited = [False] * (n + 1)
    visited[max_distance_node] = True
    dfs(max_distance_node, 0)

    tree_distance = max_distance

    print(tree_distance)