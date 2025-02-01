import sys
import math

n = int(sys.stdin.readline())
cnt = 4

for i in range(int(math.sqrt(n)), 0, -1):
    if int(math.sqrt(n)) == math.sqrt(n):
        cnt = 1
        break
    elif int(math.sqrt(n - i ** 2)) == math.sqrt(n - i ** 2):
        cnt = 2
        break
    else:
        for j in range(int(math.sqrt(n - i ** 2)), 0, -1):
            if int(math.sqrt(n - i ** 2 - j ** 2)) == math.sqrt(n - i ** 2 - j ** 2):
                cnt = 3
                break
print(cnt)