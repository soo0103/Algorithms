import sys

def length(x1, x2, y1, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        coordinates = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

        coordinates.sort()

        d1 = length(coordinates[0][0], coordinates[3][0], coordinates[0][1], coordinates[3][1])
        d2 = length(coordinates[1][0], coordinates[2][0], coordinates[1][1], coordinates[2][1])

        s1 = length(coordinates[0][0], coordinates[1][0], coordinates[0][1], coordinates[1][1])
        s2 = length(coordinates[0][0], coordinates[2][0], coordinates[0][1], coordinates[2][1])
        s3 = length(coordinates[3][0], coordinates[1][0], coordinates[3][1], coordinates[1][1])
        s4 = length(coordinates[3][0], coordinates[2][0], coordinates[3][1], coordinates[2][1])

        if s1 == s2 == s3 == s4 and d1 == d2:
            print(1)
        else:
            print(0)