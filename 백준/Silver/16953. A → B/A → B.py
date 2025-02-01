import sys
from collections import deque

def bfs(A, B):
    dq = deque()
    dq.append((A, 0))
    
    while dq:
        num, cnt = dq.popleft()
        
        if num == B:
            print(cnt + 1)
            return
        
        if num > B:
            continue
                
        dq.append((num * 2, cnt + 1))
        dq.append((num * 10 + 1, cnt + 1))
    
    print(-1)

if __name__ == "__main__":
    A, B = map(int, sys.stdin.readline().split())
    
    bfs(A, B)