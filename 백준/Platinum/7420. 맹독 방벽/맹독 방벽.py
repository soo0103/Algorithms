import sys

PI = 3.1415926535

def crossProduct(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1

def ccw(x1, y1, x2, y2, x3, y3):
    value = crossProduct(x2 - x1, y2 - y1, x3 - x1, y3 - y1)

    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0

def getDistance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

def getConvexhull(points):
    points.sort()

    s1 = []
    s2 = []

    for x, y in points:
        while len(s1) >= 2 and ccw(s1[-2][0], s1[-2][1], s1[-1][0], s1[-1][1], x, y) <= 0:
            s1.pop()

        s1.append([x, y])

    for x, y in reversed(points):
        while len(s2) >= 2 and ccw(s2[-2][0], s2[-2][1], s2[-1][0], s2[-1][1], x, y) <= 0:
            s2.pop()

        s2.append([x, y])

    convexHull = s1[:-1] + s2[:-1]

    return convexHull

if __name__ == "__main__":
    N, L = map(int, sys.stdin.readline().split())
    buildings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    convexHull = getConvexhull(buildings)

    length = 2 * PI * L
    start = [buildings[0][0], buildings[0][1]]
    convexHull.append(start)

    for i in range(1, len(convexHull)):
        length += getDistance(start, convexHull[i])
        start = convexHull[i]

    print(int(round(length, 0)))