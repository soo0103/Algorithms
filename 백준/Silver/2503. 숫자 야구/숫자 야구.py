import sys
from itertools import permutations

N = int(sys.stdin.readline())
baseball = list(permutations(list(range(1, 10)), 3))

for i in range(N):
    num, strike, ball = map(int, sys.stdin.readline().split())
    tmp = []

    for j in baseball:
        s, b = 0, 0

        for k, number in enumerate(str(num)):
            if int(number) == j[k]:
                s += 1
            if int(number) != j[k] and int(number) in j:
                b += 1

        if s == strike and b == ball:
            tmp.append(j)

    baseball = tmp

print(len(baseball))