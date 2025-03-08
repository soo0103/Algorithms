import sys

N = int(sys.stdin.readline())

result = 0
cnt = 1
end = 1

for i in range(N):
    while result < N and end < N:
        result += end
        end += 1
    
    if result == N:
        cnt += 1
    
    result -= i + 1

print(cnt)