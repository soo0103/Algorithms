import sys
sys.setrecursionlimit(10 ** 6)

def dfs(current_node, cost):
    global max_distance, max_distance_node

    if cost > max_distance:
        max_distance = cost
        max_distance_node = current_node

    for next_node, weight in graph[current_node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, cost + weight)

if __name__ == "__main__":
    V = int(sys.stdin.readline())

    graph = [[] for _ in range(V + 1)]
    max_distance = 0
    max_distance_node = 0

    for _ in range(V):
        edge = list(map(int, sys.stdin.readline().split()))
        i = 1
        while edge[i] != -1:
            graph[edge[0]].append((edge[i], edge[i + 1]))
            graph[edge[i]].append((edge[0], edge[i + 1]))
            i += 2

    visited = [False] * (V + 1)
    visited[1] = True
    dfs(1, 0)

    visited = [False] * (V + 1)
    visited[max_distance_node] = True
    dfs(max_distance_node, 0)

    tree_distance = max_distance

    print(tree_distance)