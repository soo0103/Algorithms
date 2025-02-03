import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in A:
    cnt += i // 2

    if i % 2 == 1:
        cnt += 1
    
if cnt >= N:
    print("YES")
else:
    print("NO")