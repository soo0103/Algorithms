import sys

N, M, B = map(int, sys.stdin.readline().split())

ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
INF = int(1e9)
height = 0
time = INF

for h in range(257):
    obtained = 0
    used = 0
    
    for i in ground:
        for j in i:
            if j > h:
                obtained += j - h
            else:
                used += h - j
                
    if obtained + B >= used:
        if obtained * 2 + used <= time:
            time = obtained * 2 + used
            height = h

print(time, height)