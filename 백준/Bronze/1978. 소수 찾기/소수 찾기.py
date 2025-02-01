import sys

N = map(int, sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in arr:
    flag = True

    if i == 1:
        continue

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            flag = False
            break
    
    if flag:
        cnt += 1

print(cnt)