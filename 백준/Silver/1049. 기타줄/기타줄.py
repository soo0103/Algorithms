import sys

N, M = map(int, sys.stdin.readline().split())

package = []
each = []
cost = 0

for _ in range(M):
    p, e = map(int, sys.stdin.readline().split())

    package.append(p)
    each.append(e)

while N > 0:
    if N >= 6:
        cost += min(min(each) * 6, min(package))
        N -= 6
    else:
        cost += min(min(each) * N, min(package))
        N -= N

print(cost)