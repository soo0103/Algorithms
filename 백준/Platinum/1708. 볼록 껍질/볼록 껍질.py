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
    N = int(sys.stdin.readline())
    points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    start = min(points, key = lambda x : (x[0], x[1]))
    points.remove(start)

    points.sort(key = lambda p : (slope(start[0], start[1], p[0], p[1]), p[0], p[1]))

    stack = [start]

    for x, y in points:
        while len(stack) >= 2 and ccw(stack[-2][0], stack[-2][1], stack[-1][0], stack[-1][1], x, y) <= 0:
            stack.pop()

        stack.append([x, y])

    print(len(stack))