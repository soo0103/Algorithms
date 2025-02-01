import sys
import math

N = int(sys.stdin.readline())

fact = math.factorial(N)
fact = list(map(int, str(fact)))
cnt = 0

for i in range(len(fact) - 1, -1, -1):
    if fact[i] == 0:
        cnt += 1
    else:
        break

print(cnt)