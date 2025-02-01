import sys

def lotto(depth, idx):
    if depth == 6:
        S.sort()
        print(' '.join(map(str, S)))
        return
        
    for i in range(idx, k + 1):
        S.append(arr[i])
        lotto(depth + 1, i + 1)
        S.pop()

while 1:
    arr = list(map(int, sys.stdin.readline().split()))
    k = arr[0]
    S = []

    lotto(0, 1)

    if k == 0:
        break

    print()