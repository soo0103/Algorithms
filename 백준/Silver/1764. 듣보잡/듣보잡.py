import sys

N, M = map(int, sys.stdin.readline().split())
heard = set()
seen = set()
for _ in range(N):
    heard.add(sys.stdin.readline().strip())

for _ in range(M):
    seen.add(sys.stdin.readline().strip())

all = list(heard & seen)
all.sort()

print(len(all))
print(*all, sep='\n')