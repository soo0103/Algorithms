import sys

S = sys.stdin.readline().strip()

sub = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        sub.add(S[i:j + 1])

print(len(sub))