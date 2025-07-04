import sys
from collections import deque

INF = int(1e9)

def bfs(start, cnt):
    dq = deque()
    dq.append((start, cnt))
    visited[start] = True

    while dq:
        current, count = dq.popleft()

        if current == G:
            return count

        for next_floor in (current + U, current - D):
            if 1 <= next_floor <= F and not visited[next_floor]:
                visited[next_floor] = True
                dq.append((next_floor, count + 1))

    return INF

if __name__ == "__main__":
    F, S, G, U, D = map(int, sys.stdin.readline().split())

    visited = [False] * (F + 1)
    dist = [0] * (F + 1)

    result = bfs(S, 0)

    if result == INF:
        print("use the stairs")
    else:
        print(result)