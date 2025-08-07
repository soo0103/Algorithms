import sys

def move(r, c, s, d):
    nr, nc, nd = r, c, d
    
    if d == 1:
        if s <= r - 1:
            nr -= s
        else:
            rest = s - (r - 1)
            if ((rest - 1) // (R - 1)) % 2 == 0:
                nd = 2
            if (rest // (R - 1)) % 2 == 1:
                nr = R - rest % (R - 1)
            else:
                nr = 1 + rest % (R - 1)
                
    elif d == 2:
        if s <= R - r:
            nr += s
        else:
            rest = s - (R - r)
            if ((rest - 1) // (R - 1)) % 2 == 0:
                nd = 1
            if (rest // (R - 1)) % 2 == 1:
                nr = 1 + rest % (R - 1)                
            else:
                nr = R - rest % (R - 1)

    elif d == 3:
        if s <= C - c:
            nc += s
        else:
            rest = s - (C - c)
            if ((rest - 1) // (C - 1)) % 2 == 0:
                nd = 4
            if (rest // (C - 1)) % 2 == 1:
                nc = 1 + rest % (C - 1)
            else:
                nc = C - rest % (C - 1)

    elif d == 4:
        if s <= c - 1:
            nc -= s
        else:
            rest = s - (c - 1)
            if ((rest - 1) // (C - 1)) % 2 == 0:
                nd = 3
            if (rest // (C - 1)) % 2 == 1:
                nc = C - rest % (C - 1)
            else:
                nc = 1 + rest % (C - 1)
                
    return (nr, nc, nd)
        
if __name__ == "__main__":
    R, C, M = map(int, sys.stdin.readline().split())

    lattice = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
    total_size = 0

    for _ in range(M):
        r, c, s, d, z = map(int, sys.stdin.readline().split())
        lattice[r][c] = [s, d, z]

    for current in range(1, C + 1):
        for i in range(1, R + 1):
            if lattice[i][current]:
                total_size += lattice[i][current][2]
                lattice[i][current] = []
                break
            
        temp_lattice = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
        
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                if lattice[r][c]:
                    nr, nc, nd = move(r, c, lattice[r][c][0], lattice[r][c][1])
                    if not temp_lattice[nr][nc] or temp_lattice[nr][nc][2] < lattice[r][c][2]:
                        temp_lattice[nr][nc] = [lattice[r][c][0], nd, lattice[r][c][2]]
            
        lattice = temp_lattice

    print(total_size)