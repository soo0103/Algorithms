import sys

def DnC(x, y, N):
    global minus, zero, plus
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                DnC(x, y, N // 3)
                DnC(x, y + N // 3, N // 3)
                DnC(x, y + 2 * (N // 3), N // 3)
                DnC(x + N // 3, y, N // 3)
                DnC(x + N // 3, y + N // 3, N // 3)
                DnC(x + N // 3, y + 2 * (N // 3), N // 3)
                DnC(x + 2 * (N // 3), y, N // 3)
                DnC(x + 2 * (N // 3), y + N // 3, N // 3)
                DnC(x + 2 * (N // 3), y + 2 * (N // 3), N // 3)
                return

    if color == -1:
        minus += 1
    elif color == 0:
        zero += 1
    else:
        plus += 1
        
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    paper = []

    for _ in range(N):
        paper.append(list(map(int, sys.stdin.readline().split())))

    minus = 0
    zero = 0
    plus = 0

    DnC(0, 0, N)
    
    print(minus)
    print(zero)
    print(plus)