import sys

N, L, H = map(int, sys.stdin.readline().split())
score = sorted(list(map(int, sys.stdin.readline().split())))

final = sum(score)

if L != 0:
    final -= sum(score[:L])
if H != 0:
    final -= sum(score[-H:])

print(final / (len(score) - (L + H)))