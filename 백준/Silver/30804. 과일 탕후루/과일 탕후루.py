import sys

N = int(sys.stdin.readline())

fruit = list(map(int, sys.stdin.readline().split()))
count = [0 for _ in range(10)]

start = 0
end = 0
kind = 0
cnt = 0

while end < N:
    if count[fruit[end]] == 0:
        kind += 1
    count[fruit[end]] += 1
    
    while kind > 2:
        count[fruit[start]] -= 1
        if count[fruit[start]] == 0:
            kind -= 1
        start += 1
        
    cnt = max(cnt, end - start + 1)
    end += 1
    
print(cnt)