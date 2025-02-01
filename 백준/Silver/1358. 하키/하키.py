import sys

W, H, X, Y, P = map(int, sys.stdin.readline().split())

cnt = 0

for _ in range(P):
    x, y = map(int ,sys.stdin.readline().split())

    if Y <= y <= Y + H and X <= x <= X + W:
        cnt += 1
    elif y > Y + H or y < Y:
        continue
    elif x < X:
        if ((X - x) ** 2 + (Y + H // 2 - y) ** 2) ** 0.5 <= H // 2:
            cnt += 1
    elif x > X + W:
        if ((X + W - x) ** 2 + (Y + H // 2 - y) ** 2) ** 0.5 <= H // 2:
            cnt += 1

print(cnt)