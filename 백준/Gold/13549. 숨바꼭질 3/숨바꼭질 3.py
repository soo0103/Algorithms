import sys
from collections import deque

def bfs(now):
    dq = deque()
    dq.append(now)
    
    while dq:
        n = dq.popleft()

        if n == K:
            return time[K]
        
        for i in (n * 2, n - 1, n + 1):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = True
                
                if i == n * 2:
                    time[i] = time[n]
                    dq.appendleft(i)
                else:
                    time[i] = time[n] + 1
                    dq.append(i)

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    time = [0] * 100001
    visited = [False] * 100001
    print(bfs(N))