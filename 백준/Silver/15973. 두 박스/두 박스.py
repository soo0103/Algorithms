import sys

def isIntersect(p1, p2, p3, p4):
    if p2 < p3 or p1 > p4:
        return -1
    elif p2 == p3 or p1 == p4:
        return 0
    else:
        return 1

if __name__ == "__main__":
    P = list(map(int, sys.stdin.readline().split()))
    Q = list(map(int, sys.stdin.readline().split()))

    X = isIntersect(P[0], P[2], Q[0], Q[2])
    Y = isIntersect(P[1], P[3], Q[1], Q[3])

    if X == -1 or Y == -1:
        print("NULL")
    else:
        if not X:
            if not Y:
                print("POINT")
            else:
                print("LINE")
        else:
            if not Y:
                print("LINE")
            else:
                print("FACE")