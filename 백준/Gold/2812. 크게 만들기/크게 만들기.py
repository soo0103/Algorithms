import sys

N, K = map(int, sys.stdin.readline().split())
num = sys.stdin.readline().strip()

s = []

for n in num:
    while s and s[-1] < n and K > 0:
        s.pop()
        K -= 1
    
    s.append(n)

if K > 0:
    print(*s[:-K], sep = '')
else:
    print(*s, sep = '')