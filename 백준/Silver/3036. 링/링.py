import sys

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

N = int(sys.stdin.readline())
rings = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    divisor = gcd(rings[0], rings[i])
    print(f"{rings[0] // divisor}/{rings[i] // divisor}")