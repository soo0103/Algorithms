import sys

N = int(sys.stdin.readline())

for _ in range(N):
    K = int(sys.stdin.readline())
    
    if K % 2 == 0:
        print("even")
    else:
        print("odd")