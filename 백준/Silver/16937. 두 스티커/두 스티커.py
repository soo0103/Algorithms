import sys

H, W = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
stickers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

area = 0

for i in range(N):
    R1, C1 = stickers[i]

    for j in range(i + 1, N):
        R2, C2 = stickers[j]
    
        cases = [(R1, C1, R2, C2), (R1, C1, C2, R2), (C1, R1, R2, C2), (C1, R1, C2, R2)]

        for r1, c1, r2, c2 in cases:
            if (r1 + r2 <= H and max(c1, c2) <= W) or (max(r1, r2) <= H and c1 + c2 <= W):
                area = max(area, r1 * c1 + r2 * c2)

            if (r1 + r2 <= W and max(c1, c2) <= H) or (max(r1, r2) <= W and c1 + c2 <= H):
                area = max(area, r1 * c1 + r2 * c2)

print(area)