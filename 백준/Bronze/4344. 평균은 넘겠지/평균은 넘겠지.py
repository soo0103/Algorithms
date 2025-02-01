import sys

C = int(sys.stdin.readline())

for _ in range(C):
    arr = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    avg = sum(arr[1:]) / arr[0]

    for score in arr[1:]:
        if score > avg:
            cnt += 1

    rate = cnt / len(arr[1:])
    print(f"{rate * 100:.3f}%")