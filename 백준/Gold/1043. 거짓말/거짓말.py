import sys

N, M = map(int, sys.stdin.readline().split())
knowns = set(map(int, sys.stdin.readline().split()[1:]))
parties = [set(map(int, sys.stdin.readline().split()[1:])) for _ in range(M)]

cnt = 0

for _ in range(M):
    for party in parties:
        if party & knowns:
            knowns = knowns.union(party)

for party in parties:
    if party & knowns:
        continue
    cnt += 1

print(cnt)