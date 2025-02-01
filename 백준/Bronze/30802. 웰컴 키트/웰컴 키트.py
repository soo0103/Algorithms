import sys
import math

N = int(sys.stdin.readline())
S, M, L, XL, XXL, XXXL = map(int, sys.stdin.readline().split())
T, P = map(int, sys.stdin.readline().split())

print(math.ceil(S / T) + math.ceil(M / T) + math.ceil(L / T) + math.ceil(XL / T) + math.ceil(XXL / T) + math.ceil(XXXL / T))
print(N // P, N % P)