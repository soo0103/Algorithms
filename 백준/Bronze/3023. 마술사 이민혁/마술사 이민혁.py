import sys

R, C = map(int, sys.stdin.readline().split())

arr = [[0] * (2 * C) for _ in range(2 * R)]

for i in range(R):
    word = sys.stdin.readline().strip()
    
    for j in range(C):
        arr[i][j] = word[j]
        arr[i][-1 - j] = word[j]
        arr[-1 - i][j] = word[j]
        arr[-1 - i ][-1 - j] = word[j]

x, y = map(int, sys.stdin.readline().split())

if arr[x - 1][y - 1] == ".":
    arr[x - 1][y - 1] = "#"
else:
    arr[x - 1][y - 1] = "."

for i in range(2 * R):
    print("".join(arr[i]))