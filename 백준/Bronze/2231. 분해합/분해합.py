import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    num = sum(map(int, str(i)))
    value = i + num
    
    if value == N:
        print(i)
        break

    if i == N:
        print(0)