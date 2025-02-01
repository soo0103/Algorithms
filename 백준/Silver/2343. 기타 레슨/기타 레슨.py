import sys

N, M = map(int, sys.stdin.readline().split())
lecture = list(map(int, sys.stdin.readline().split()))

start = max(lecture)
end = sum(lecture)
result = 0

while start <= end:
    mid = (start + end) // 2
    time = 0
    cnt = 1

    for i in lecture:
        if time + i > mid:
            cnt += 1
            time = 0
        time += i

    if cnt <= M:
        end = mid - 1
        result = mid
    else:
        start = mid + 1
        
print(result)