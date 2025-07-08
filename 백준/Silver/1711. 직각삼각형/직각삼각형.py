import sys

def is_right(p1, p2, p3):
    s1 = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    s2 = (p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2
    s3 = (p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2

    if s1 + s2 == s3 or s1 + s3 == s2 or s2 + s3 == s1:
        return True
    else:
        return False

N = int(sys.stdin.readline())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            cnt += is_right(points[i], points[j], points[k])

print(cnt)