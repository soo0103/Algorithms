import sys

def crossProduct(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1

def isBetween(a, b, c):
    return min(a, b) <= c <= max(a, b)

def ccw(x1, y1, x2, y2, x3, y3):
    value = crossProduct(x2 - x1, y2 - y1, x3 - x1, y3 - y1)

    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0

if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

    d1 = ccw(x1, y1, x2, y2, x3, y3)
    d2 = ccw(x1, y1, x2, y2, x4, y4)
    d3 = ccw(x3, y3, x4, y4, x1, y1)
    d4 = ccw(x3, y3, x4, y4, x2, y2)

    if d1 * d2 < 0 and d3 * d4 < 0:
        print(1)
    elif d1 == 0 and isBetween(x1, x2, x3) and isBetween(y1, y2, y3):
        print(1)
    elif d2 == 0 and isBetween(x1, x2, x4) and isBetween(y1, y2, y4):
        print(1)
    elif d3 == 0 and isBetween(x3, x4, x1) and isBetween(y3, y4, y1):
        print(1)
    elif d4 == 0 and isBetween(x3, x4, x2) and isBetween(y3, y4, y2):
        print(1)
    else:
        print(0)