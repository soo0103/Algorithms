import sys

num = []

for _ in range(10):
    n = int(sys.stdin.readline()) % 42

    if n not in num:
        num.append(n)

print(len(num))