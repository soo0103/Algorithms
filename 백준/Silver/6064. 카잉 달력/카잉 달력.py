import sys

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    
    nm = max(N, M)
    
    if nm == M:
        xy = x
    else:
        xy = y

    while xy <= M * N:
        if (xy - x) % M == 0 and (xy - y) % N == 0:
            print(xy)
            break
        xy += nm
        
    if xy > M * N:
        print(-1)