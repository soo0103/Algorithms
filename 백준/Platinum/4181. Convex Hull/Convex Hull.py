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

def slope(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    
    if dx == 0:
        return float('inf')

    return dy / dx

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    points = []

    for _ in range(n):
        x, y, c = sys.stdin.readline().split()

        if c == 'Y':
            points.append([int(x), int(y)])

    start = min(points, key = lambda x : (x[0], x[1]))
    points.remove(start)

    points.sort(key = lambda p : (slope(start[0], start[1], p[0], p[1]), p[0], p[1]))

    s1 = [start]
    s2 = []

    for x, y in points:
        while len(s1) >= 2 and ccw(s1[-2][0], s1[-2][1], s1[-1][0], s1[-1][1], x, y) < 0:
            s1.pop()

        s1.append([x, y])

    for x, y in reversed(points):
        while len(s2) >= 2 and ccw(s2[-2][0], s2[-2][1], s2[-1][0], s2[-1][1], x, y) < 0:
            s2.pop()

        s2.append([x, y])

    result = s1[:-1] + s2[:-1]

    print(len(result))
    
    for x, y in result:
        print(x, y)