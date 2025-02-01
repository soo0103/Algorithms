import sys

def tile(n):
    if arr[n]:
        return arr[n]

    arr[n] = (tile(n - 1) + tile(n - 2)) % 10007

    return arr[n]

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        arr = [0] * (n + 1)
        arr[1] = 1
        arr[2] = 2
        print(tile(n))