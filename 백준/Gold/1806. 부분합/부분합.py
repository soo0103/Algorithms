import sys

INF = int(1e9)

N, S = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
result = seq[0]
length = INF

while 1:
    if result >= S:
        length = min(length, end - start + 1)
        result -= seq[start]
        start += 1
    else:
        end += 1

        if end == N:
            break
        
        result += seq[end]

if length == INF:
    print(0)
else:
    print(length)