import sys
from fractions import Fraction

C = 300000

N = int(sys.stdin.readline())

m2 = N ** 2
u1, u2 = 0, -C
cnt = 0

while 1:
    if u2 - u1 >= 0:
        break

    v1 = Fraction((1 - m2), (1 + m2)) * u1 + Fraction((2 * m2), (1 + m2)) * u2
    v2 = Fraction(2, (1 + m2)) * u1 - Fraction((1 - m2), (1 + m2)) * u2
    cnt += 1

    u1 = v1
    u2 = v2

    if u1 <= 0:
        if u1 < 0:
            cnt += 1
        u1 = -u1

print(cnt)