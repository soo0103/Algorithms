import sys

xa, ya, xb, yb, xc, yc = map(int, sys.stdin.readline().split())

ab = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
bc = ((xb - xc) ** 2 + (yb - yc) ** 2) ** 0.5
ac = ((xa - xc) ** 2 + (ya - yc) ** 2) ** 0.5

if (xa - xb) * (ya - yc) == (ya - yb) * (xa -xc):
    print(-1.0)
else:
    l1 = max(ab + bc, ab + ac, ac + bc)
    l2 = min(ab + bc, ab + ac, ac + bc)

    print(2 * (l1 - l2))