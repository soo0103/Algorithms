import sys

S = sys.stdin.readline().strip()

suffix = []

for i in range(len(S)):
    suffix.append(S[i:])

suffix.sort()

print(*suffix, sep = '\n')