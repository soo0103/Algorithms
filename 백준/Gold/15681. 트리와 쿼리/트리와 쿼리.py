import sys
sys.setrecursionlimit(10 ** 6)

def make_tree(current_node, parent):
    for node in connect[current_node]:
        if node != parent:
            child[current_node].append(node)
            parents[node] = current_node
            make_tree(node, current_node)

def count_subtree_nodes(current_node):
    size[current_node] = 1
    for node in child[current_node]:
        count_subtree_nodes(node)
        size[current_node] += size[node]

if __name__ == "__main__":
    N, R, Q = map(int, sys.stdin.readline().split())

    connect = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        U, V = map(int, sys.stdin.readline().split())
        connect[U].append(V)
        connect[V].append(U)

    queries = [int(sys.stdin.readline()) for _ in range(Q)]

    size = [0] * (N + 1)
    child = [[] for _ in range(N + 1)]
    parents = [i for i in range(N + 1)]

    make_tree(R, -1)
    count_subtree_nodes(R)
    
    for query in queries:
        print(size[query])