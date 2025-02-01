import sys

n = int(sys.stdin.readline())

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())

    print(f"Scenario #{i + 1}:")

    if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
        print("yes\n")
    else:
        print("no\n")