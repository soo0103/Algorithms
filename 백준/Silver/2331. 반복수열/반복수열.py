import sys

A, P = map(int, sys.stdin.readline().split())

arr = [A]

while 1:
    temp = 0

    for i in str(arr[-1]):
        temp += int(i) ** P

    if temp in arr:
        break

    arr.append(temp)

print(arr.index(temp))