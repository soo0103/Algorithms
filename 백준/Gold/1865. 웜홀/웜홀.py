import sys

INF = int(1e9)

def bellman_ford(start):
    distance[start] = 0

    for i in range(N):
        for current_node in range(1, N + 1):
            for next_node, cost in graph[current_node]:
                if distance[next_node] > distance[current_node] + cost:
                    distance[next_node] = distance[current_node] + cost
                
                    if i == N - 1:
                        return True
                    
    return False

if __name__ == "__main__":
    TC = int(sys.stdin.readline())

    for _ in range(TC):
        N, M, W = map(int, sys.stdin.readline().split())

        graph = [[] for _ in range(N + 1)]
        distance = [INF] * (N + 1)

        for i in range(M + W):
            S, E, T = map(int, sys.stdin.readline().split())

            if i >= M:
                T = -T
            else:
                graph[E].append((S, T))
            graph[S].append((E, T))

        if bellman_ford(1):
            print("YES")
        else:
            print("NO")