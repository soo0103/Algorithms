import sys

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

def rotatingCalipers(convexHull):
    lp, rp = 0, 1
    size = len(convexHull)
    distance = 0

    while lp < size:
        llx, lly = convexHull[(lp + 1) % size]
        lx, ly = convexHull[lp]

        while 1:
            comp = getDistance(convexHull[lp], convexHull[rp])
            if distance < comp:
                distance = comp
                pair = [convexHull[lp], convexHull[rp]]

            rrx, rry = convexHull[(rp + 1) % size]
            rx, ry = convexHull[rp]

            if crossProduct(llx - lx, lly - ly, rrx - rx, rry - ry) > 0:
                rp = (rp + 1) % size
            else:
                lp += 1
                break

    return pair

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        n = int(sys.stdin.readline())

        cities = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

        if len(cities) > 2:
            convexHull = getConvexhull(cities)
            pair = rotatingCalipers(convexHull)
        else:
            pair = [cities[0], cities[1]]
        
        print(pair[0][0], pair[0][1], pair[1][0], pair[1][1])