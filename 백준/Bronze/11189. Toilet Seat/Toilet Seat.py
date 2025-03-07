import sys

toilet = sys.stdin.readline().strip()

u, d, c = 0, 0, 0

if toilet[0] == 'U':
    if toilet[1] == 'U':
        d += 1
    else:
        u += 2
        d += 1
else:
    if toilet[1] == 'U':
        u += 1
        d += 2
    else:
        u += 1

for i in toilet[2:]:
    if i != 'U':
        u += 2

for i in toilet[2:]:
    if i != 'D':
        d += 2

for i in range(len(toilet) - 1):
    if toilet[i] != toilet[i + 1]:
        c += 1

print(u)
print(d)
print(c)