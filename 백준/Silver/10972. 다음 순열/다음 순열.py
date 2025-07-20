import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

flag = False

for i in range(N - 1, 0, -1):
    if arr[i - 1] < arr[i]:
        for j in range(N - 1, 0, -1):
            if arr[i - 1] < arr[j]:
                arr[i - 1], arr[j] = arr[j], arr[i - 1]
                arr = arr[:i] + sorted(arr[i:])
                flag = True
                break
    
    if flag:
        break

if flag:
    print(*arr)
else:
    print(-1)