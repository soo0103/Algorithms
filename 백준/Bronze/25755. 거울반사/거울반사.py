import sys

W, N = sys.stdin.readline().split()
N = int(N)
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

if W in ("U", "D"):
    for r in range(N // 2):
        arr[r], arr[N - 1 - r] = arr[N - 1 - r], arr[r]
else:
    for row in arr:
        for c in range(N // 2):
            row[c], row[N - 1 - c] = row[N - 1 - c], row[c]

for r in range(N):
    for c in range(N):
        if arr[r][c] == 2:
            arr[r][c] = 5
        elif arr[r][c] == 5:
            arr[r][c]  = 2
        elif arr[r][c] == 1 or arr[r][c] == 8:
            continue
        else:
            arr[r][c] = '?'

for i in arr:
    print(*i)