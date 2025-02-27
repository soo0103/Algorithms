import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    numbers = [sys.stdin.readline().strip() for _ in range(n)]
    numbers.sort()

    flag = True

    for i in range(n - 1):
        if numbers[i] == numbers[i + 1][:len(numbers[i])]:
            print("NO")
            flag = False
            break

    if flag:
        print("YES")