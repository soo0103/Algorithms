import sys

N = int(sys.stdin.readline())
arr = list(map(int, input().split()))
quo = sum(arr) // 3
cnt = 0

if sum(arr) % 3 == 0:
    for i in arr:
        cnt += i // 2

    if cnt >= quo:
        print("YES")
    else:
        print("NO")
else:
    print("NO")