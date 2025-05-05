import sys

def get_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

if __name__ == "__main__":
    A1, B1 = map(int, sys.stdin.readline().split())
    A2, B2 = map(int, sys.stdin.readline().split())

    n = A1 * B2 + A2 * B1
    d = B1 * B2

    gcd = get_gcd(n, d)

    print(n // gcd, d // gcd)