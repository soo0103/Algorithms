import sys

T = int(sys.stdin.readline())

for _ in range(T):
    R, S = map(str, sys.stdin.readline().split())
    R = int(R)
    
    for i in S:
        print(i * R, end='')
        
    print()