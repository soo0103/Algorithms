import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    flights = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    
    print(N - 1)