import sys

S, P = map(int, sys.stdin.readline().split())
DNA = sys.stdin.readline().strip()
contains = list(map(int, sys.stdin.readline().split()))

cnt = 0
exists = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in range(P):
    exists[DNA[i]] += 1

if exists['A'] >= contains[0] and exists['C'] >= contains[1] and exists['G'] >= contains[2] and exists['T'] >= contains[3]:
    cnt += 1

for j in range(1, S - P + 1):
    exists[DNA[j - 1]] -= 1
    exists[DNA[j + P - 1]] += 1

    if exists['A'] >= contains[0] and exists['C'] >= contains[1] and exists['G'] >= contains[2] and exists['T'] >= contains[3]:
        cnt += 1

print(cnt)