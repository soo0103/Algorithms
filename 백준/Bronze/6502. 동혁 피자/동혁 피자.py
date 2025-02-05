import sys

PI = 3.141592
i = 1

while 1:
    arr = list(map(int, sys.stdin.readline().split()))

    if arr[0] == 0:
        break
    else:
        r, w, l = arr

    diagonal = ((w ** 2 + l ** 2) ** 0.5) / 2

    if diagonal <= r:
        print(f"Pizza {i} fits on the table.")
    else:
        print(f"Pizza {i} does not fit on the table.")

    i += 1