import sys
from collections import deque

def bfs(x):
    global result, cnt
    dq = deque()
    dq.append(x)

    while dq:
        current_location = dq.popleft()

        if current_location == K:
            result = visited[current_location]
            cnt += 1
            continue

        for next_location in (current_location - 1, current_location + 1, 2 * current_location):
            if 0 <= next_location <= 100000 and (visited[next_location] == 0 or visited[current_location] + 1 == visited[next_location]):
                visited[next_location] = visited[current_location] + 1
                dq.append(next_location)

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())

    visited = [0] * 100001
    result = 0
    cnt = 0

    bfs(N)

    print(result)
    print(cnt)