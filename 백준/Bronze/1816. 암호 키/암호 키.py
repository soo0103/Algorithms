import sys

N = int(sys.stdin.readline())
S = [int(sys.stdin.readline()) for _ in range(N)]

for s in S:
    flag = True

    for i in range(2, 1000001):
        if s % i == 0:
            flag = False
            break
    
    if flag:
        print("YES")
    else:
        print("NO")