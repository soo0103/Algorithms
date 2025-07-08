import sys
from collections import defaultdict
from math import gcd

def normalize(dx, dy):
    if dx == 0 and dy == 0:
        return (0, 0)
    
    g = gcd(dx, dy)
    dx //= g
    dy //= g

    if dx < 0 or (dx == 0 and dy < 0):
        dx *= -1
        dy *= -1
    return (dx, dy)

def count_right_triangles(points):
    N = len(points)
    cnt = 0

    for i in range(N):
        slopes = defaultdict(int)
        xi, yi = points[i]
        for j in range(N):
            if i == j:
                continue
            xj, yj = points[j]
            dx = xj - xi
            dy = yj - yi
            dir = normalize(dx, dy)
            slopes[dir] += 1

        for (dx, dy), count1 in slopes.items():
            perp = normalize(-dy, dx)
            count2 = slopes.get(perp, 0)
            cnt += count1 * count2

    return cnt // 2

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(count_right_triangles(points))