import sys

N, C = map(int, sys.stdin.readline().split())
house = []

for _ in range(N):
    house.append(int(sys.stdin.readline()))

house.sort()

start = 1
end = max(house) - min(house)

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    current = house[0]

    for i in range(1, N):
        if house[i] >= current + mid:
            cnt += 1
            current = house[i]

    if cnt >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
        
print(result)