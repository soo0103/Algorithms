import sys
import math

M, N = map(int, sys.stdin.readline().split())

print(math.gcd(M, N))
print(math.lcm(M, N))