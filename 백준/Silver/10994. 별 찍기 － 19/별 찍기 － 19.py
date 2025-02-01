import sys

N = int(sys.stdin.readline())

length = 4 * N - 3
arr = [[' '] * length for _ in range(length)]
x = 0
y = 0

if length == 1:
    arr[x][y] = '*'
else:
    for i in range(length, 1, -4):
        for j in range(i):
            arr[2 * N - 2][2 * N - 2] = '*'
            arr[x][y + j] = '*'
            arr[x + i - 1][y + j] = '*'
            arr[x + j][y] = '*'
            arr[x + j][y + i - 1] = '*'
        
        x += 2
        y += 2

for k in range(length):
    print(''.join(arr[k]))
