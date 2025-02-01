import sys

T = int(sys.stdin.readline())

for _ in range(T):
    box = []
    cnt = 0
    J, N = map(int, sys.stdin.readline().split())
    
    for _ in range(N):
        R, C = map(int, sys.stdin.readline().split())
        box.append(R * C)
    
    box.sort(reverse = True)
    
    for i in box:
        J -= i
        cnt += 1
        if J <= 0:
            break
    
    print(cnt)