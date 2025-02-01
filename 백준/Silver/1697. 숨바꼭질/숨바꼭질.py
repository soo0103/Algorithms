import sys
from collections import deque

def bfs(N):
    dq.append(N)

    while 1:
        location = dq.popleft()

        if location == K:
            print(time[location])
            return
            
        for i in (location - 1, location + 1, location * 2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = True
                dq.append(i)
                time[i] = time[location] + 1

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    dq = deque()
    visited = [False] * 100001
    time = [0] * 100001
    
    bfs(N)