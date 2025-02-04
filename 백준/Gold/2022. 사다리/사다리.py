import sys

def calc(x, y, w):
    xw = (x ** 2 - w ** 2) ** 0.5
    yw = (y ** 2 - w ** 2) ** 0.5

    return xw * yw / (xw + yw)

if __name__ == "__main__":
    x, y, c = map(float, sys.stdin.readline().split())

    start = 0
    end = min(x, y)
    value = 0

    while end - start > 1e-3:
        mid = (start + end) / 2

        if calc(x, y, mid) >= c:
            start = mid
            value = mid
        else:
            end = mid

    print(value)