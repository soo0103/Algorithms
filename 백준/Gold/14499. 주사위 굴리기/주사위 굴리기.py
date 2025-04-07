import sys

def roll_dice(direction):
    p1, p2, p3, p4, p5, p6 = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if direction == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = p4, p2, p1, p6, p5, p3 
    elif direction == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = p3, p2, p6, p1, p5, p4
    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = p5, p1, p3, p4, p6, p2
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = p2, p6, p3, p4, p1, p5

if __name__ == "__main__":
    N, M, x, y, K = map(int, sys.stdin.readline().split())
    guidance = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    commands = list(map(int, sys.stdin.readline().split()))

    dice = [0, 0, 0, 0, 0, 0]
    directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    nr, nc = x, y

    for i in commands:
        nr += directions[i - 1][0]
        nc += directions[i - 1][1]

        if 0 <= nr < N and 0 <= nc < M:
            roll_dice(i)

            if guidance[nr][nc] == 0:
                guidance[nr][nc] = dice[5]
            else:
                dice[5] = guidance[nr][nc]
                guidance[nr][nc] = 0
            
            print(dice[0])
        else:
            nr -= directions[i - 1][0]
            nc -= directions[i - 1][1]