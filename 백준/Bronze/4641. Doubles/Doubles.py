import sys

while 1:
    arr = list(map(int, sys.stdin.readline().split()))

    cnt = 0

    if arr[0] == -1:
        break

    for i in arr[:-1]:
        if i * 2 in arr:
            cnt += 1

    print(cnt)