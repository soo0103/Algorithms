import sys

N = int(sys.stdin.readline())
num = 1
count = 1

while N > num:
    num += 6 * count
    count += 1

print(count)