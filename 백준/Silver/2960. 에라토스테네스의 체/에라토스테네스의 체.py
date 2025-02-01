import sys

N, K = map(int, sys.stdin.readline().split())
cnt = 0
arr = [1] * (N + 1)

for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if arr[j] != 0:
            arr[j] = 0
            cnt += 1

            if cnt == K:
                print(j)