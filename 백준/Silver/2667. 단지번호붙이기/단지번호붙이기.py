import sys

def DFS(x, y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if map[y][x] == 1:
        cnt += 1
        map[y][x] = 0
        DFS(x + 1, y)
        DFS(x, y + 1)
        DFS(x - 1, y) 
        DFS(x, y - 1)
        return True

    return False

if __name__ == "__main__":
    cnt = 0
    total = 0

    N = int(sys.stdin.readline())
    map = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

    home = []
    for i in range(N):
        for j in range(N):
            if DFS(i, j) == True:
                home.append(cnt)
                cnt = 0

    home.sort()

    print(len(home))
    
    for i in home:
        print(i)