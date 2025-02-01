import sys

def bin(N, K):
    if K == 0 or N == K:
        return 1
    else:
        return bin(N - 1, K - 1) + bin(N - 1, K)

N, K = map(int, sys.stdin.readline().split())

print(bin(N, K))