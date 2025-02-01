import sys
from collections import deque

def bfs(rr, rc, br, bc):
    dq = deque()
    dq.append((rr, rc, br, bc, 0))
    visited.append((rr, rc, br, bc))
    
    while dq:
        rr, rc, br, bc, cnt = dq.popleft()
        
        if cnt > 10:
            print(-1)
            return
        
        if board[rr][rc] == 'O':
            print(cnt)
            return
        
        for i in range(4):
            nrr = rr
            nrc = rc
            nbr = br
            nbc = bc
            
            while True:
                nrr += dr[i]
                nrc += dc[i]
                
                if board[nrr][nrc] == '#':
                    nrr -= dr[i]
                    nrc -= dc[i]
                    break
                
                if board[nrr][nrc] == 'O':
                    break
                    
            while True:
                nbr += dr[i]
                nbc += dc[i]
                
                if board[nbr][nbc] == '#':
                    nbr -= dr[i]
                    nbc -= dc[i]
                    break
                    
                if board[nbr][nbc] == 'O':
                    break
            
            if board[nbr][nbc] == 'O':
                continue
            
            if nbr == nrr and nbc == nrc:
                if abs(nrr - rr) + abs(nrc - rc) > abs(nbr - br) + abs(nbc - bc):
                    nrr -= dr[i]
                    nrc -= dc[i]
                else:
                    nbr -= dr[i]
                    nbc -= dc[i]
            
            if (nrr, nrc, nbr, nbc) not in visited:
                dq.append((nrr, nrc, nbr, nbc, cnt + 1))
                visited.append((nrr, nrc, nbr, nbc))

    print(-1)

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    board = []
    visited = []

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for _ in range(N):
        board.append(list(sys.stdin.readline().strip()))

    for r in range(N):
        for c in range(M):
            if board[r][c] == 'R':
                rr = r
                rc = c
                
            if board[r][c] == 'B':
                br = r
                bc = c

    bfs(rr, rc, br, bc)