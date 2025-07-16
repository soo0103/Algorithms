import sys

X, Y = map(int, sys.stdin.readline().split())

Z = Y * 100 // X
cnt = 0

left = 0
right = X
result = X

if Z >= 99:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2

        if 100 * (Y + mid) // (X + mid) > Z:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(result)