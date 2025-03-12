import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

result = abs(N - 100)

if M:
    broken = list(map(int, sys.stdin.readline().split()))
else:
    broken = []

for i in range(1000001):
    flag = True

    for j in str(i):
        if int(j) in broken:
            flag = False
            break
    
    if flag:
        result = min(result, len(str(i)) + abs(N - i))
    
print(result)