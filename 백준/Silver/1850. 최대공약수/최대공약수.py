import sys

def gcd(x, y):
    if x % y == 0:
        return y
    elif y == 0:
        return x
    else:
        return gcd(y, x % y)

if __name__ == "__main__":
    A, B = map(int, sys.stdin.readline().split())

    print('1' * gcd(A, B))
