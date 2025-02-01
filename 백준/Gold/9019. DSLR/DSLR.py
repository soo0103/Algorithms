import sys
from collections import deque

def bfs(inp, out):
    reg = deque()
    reg.append((inp, ''))
    visited = [False] * 10000
    visited[inp] = True
    
    while reg:
        n, cmd = reg.popleft()
        
        if n == out:
            print(cmd)
            return
        
        for command in commands:
            if command == 'D':
                d = (2 * n) % 10000
                if not visited[d]:
                    visited[d] = True
                    reg.append((d, cmd + command))
                
            if command == 'S':
                s = (n - 1) % 10000
                if not visited[s]:
                    visited[s] = True
                    reg.append((s, cmd + command))
            
            if command == 'L':
                l = n // 1000 + (n % 1000) * 10
                if not visited[l]:
                    visited[l] = True
                    reg.append((l, cmd + command))
            
            if command == 'R':
                r = (n % 10) * 1000 + n // 10
                if not visited[r]:
                    visited[r] = True
                    reg.append((r, cmd + command))

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    
    commands = ['D', 'S', 'L', 'R']

    for _ in range(T):
        inp, out = map(int, sys.stdin.readline().split())
        bfs(inp, out)