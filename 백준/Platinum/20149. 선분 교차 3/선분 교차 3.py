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

def isIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
    if ccw(x1, y1, x3, y3, x4, y4) * ccw(x2, y2, x3, y3, x4, y4) == 0:
        if ccw(x3, y3, x1, y1, x2, y2) * ccw(x4, y4, x1, y1, x2, y2) == 0:
            if (x1, y1) > (x2, y2):
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            if (x3, y3) > (x4, y4):
                x3, x4 = x4, x3
                y3, y4 = y4, y3

            if (x2, y2) >= (x3, y3) and (x1, y1) <= (x4, y4):
                return True
            else:
                return False
    
    if ccw(x1, y1, x3, y3, x4, y4) * ccw(x2, y2, x3, y3, x4, y4) <= 0:
        if ccw(x3, y3, x1, y1, x2, y2) * ccw(x4, y4, x1, y1, x2, y2) <= 0:
            return True
        
    return False

def getIntersection(x1, y1, x2, y2, x3, y3, x4, y4):
    a1 = y2 - y1
    b1 = x1 - x2
    c1 = a1 * x1 + b1 * y1
    
    a2 = y4 - y3
    b2 = x3 - x4
    c2 = a2 * x3 + b2 * y3

    D = crossProduct(a1, b1, a2, b2)
    x = crossProduct(c1, c2, b1, b2) / D
    y = crossProduct(a1, a2, c1, c2) / D

    return (x, y)

if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

    if isIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
        print(1)

        try:
            x, y = getIntersection(x1, y1, x2, y2, x3, y3, x4, y4)
            print(x, y)
        except:
            if (x1, y1) > (x2, y2):
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            if (x3, y3) > (x4, y4):
                x3, x4 = x4, x3
                y3, y4 = y4, y3

            if x2 == x3 and y2 == y3:
                print(x2, y2)
            elif x1 == x4 and y1 == y4:
                print(x1, y1)
    else:
        print(0)