import sys
from collections import deque

def bfs():
    dq = deque()
    dq.append(1)

    while dq:
        cell = dq.popleft()
        
        if cell == 100:
            print(cnt[100])
            break
        
        for i in range(1, 7):
            next = cell + i

            if next <= 100 and not visited[next]: 
                if next in jump:
                    next = jump[next]

                    if not visited[next]:
                        visited[next] = True
                        cnt[next] = cnt[cell] + 1
                        dq.append(next)
                        
                else:
                    visited[next] = True
                    cnt[next] = cnt[cell] + 1
                    dq.append(next)
                    
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    jump = {}
    visited = [False] * 101
    cnt = [0] * 101

    for i in range(N + M):
        x, y = map(int, sys.stdin.readline().split())
        jump[x] = y
        
    bfs()