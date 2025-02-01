import sys

N = int(sys.stdin.readline())
budget = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

start = 1
end = max(budget)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in budget:
        if i >= mid:
            total += mid
        else:
            total += i

    if total > M:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
        
print(result)