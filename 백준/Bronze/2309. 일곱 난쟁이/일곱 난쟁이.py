import sys

arr = []

for _ in range(9):
    arr.append(int(sys.stdin.readline()))

height = sum(arr)

for i in range(8):
    for j in range(i + 1, 9):
        if height - arr[i] - arr[j] == 100:
            rm = [arr[i], arr[j]]
            break

arr.remove(rm[0])
arr.remove(rm[1])

arr.sort()

print(*arr, sep="\n")