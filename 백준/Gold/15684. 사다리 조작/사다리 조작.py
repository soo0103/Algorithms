import sys

def is_equal():
    for i in range(N):
        current = i
        
        for j in range(H):
            if ladder[j][current]:
                current += 1
            elif current > 0 and ladder[j][current - 1]:
                current -= 1

        if current != i:
            return False
        
    return True

def dfs(row, col, cnt):
    global count

    if cnt >= MAX_COUNT:
        return

    if is_equal():
        count = min(count, cnt)
        return

    for r in range(row, H):
        if r == row:
            current = col
        else:
            current = 0
        
        for c in range(current, N - 1):
            if not ladder[r][c + 1] and not ladder[r][c]:
                if c > 0 and ladder[r][c - 1]:
                    continue

                ladder[r][c] = True
                dfs(r, c + 2, cnt + 1)
                ladder[r][c] = False

if __name__ == "__main__":
    MAX_COUNT = 4

    N, M, H = map(int, sys.stdin.readline().split())

    if H != 0:
        ladder = [[False] * N for _ in range(H)]
        
        for _ in range(M):
            a, b = map(int, sys.stdin.readline().split())
            ladder[a - 1][b - 1] = True
            
        count = MAX_COUNT
        dfs(0, 0, 0)
        
        if count < MAX_COUNT:
            print(count)
        else:
            print(-1)
    else:
        print(0)