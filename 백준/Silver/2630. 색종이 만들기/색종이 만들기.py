import sys

def DnC(x, y, N):
    global blue, white
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                DnC(x, y, N // 2)
                DnC(x, y + N // 2, N // 2)
                DnC(x + N // 2, y, N // 2)
                DnC(x + N // 2, y + N // 2, N // 2)
                return

    if color == 0:
        white += 1
    else:
        blue += 1
        
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    paper = []

    for _ in range(N):
        paper.append(list(map(int, sys.stdin.readline().split())))

    blue = 0
    white = 0

    DnC(0, 0, N)
    
    print(white)
    print(blue)