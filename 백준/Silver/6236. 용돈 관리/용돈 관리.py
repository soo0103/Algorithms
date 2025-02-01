import sys

N, M = map(int, sys.stdin.readline().split())
daily = []

for _ in range(N):
    daily.append(int(sys.stdin.readline()))

start = min(daily)
end = sum(daily)

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    charge = mid

    for i in daily:
        if charge < i:
            charge = mid
            cnt += 1
        charge -= i    

    if cnt > M or mid < max(daily):
        start = mid + 1
    else:
        end = mid - 1
        k = mid
        
print(k)