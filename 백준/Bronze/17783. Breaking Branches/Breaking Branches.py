import sys

n = int(sys.stdin.readline())

if n == 2:
    print("Alice")
    print(1)
elif n == 3:
    print("Bob")
else:
    if n % 2 == 0:
        print("Alice")
        print(n // 2 - 1)
    else:
        print("Bob")