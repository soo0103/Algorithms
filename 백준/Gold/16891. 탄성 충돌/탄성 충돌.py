import sys
from fractions import Fraction

N = int(sys.stdin.readline())

m = N ** 2
u1 = 0
u2 = -100000
cnt = 0

while 1:
    v1 = Fraction((1 - m), (1 + m)) * u1 + Fraction((2 * m), (1 + m)) * u2
    v2 = Fraction(2, (1 + m)) * u1 - Fraction((1 - m), (1 + m)) * u2
    cnt += 1

    u1 = v1
    u2 = v2

    if u1 <= 0:
        if u1 < 0:
            cnt += 1
        u1 = -u1
        
    if u2 - u1 >= 0:
        break

print(cnt)