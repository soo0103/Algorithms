import sys

N, M = map(int, sys.stdin.readline().split())
tree = tuple(map(int, sys.stdin.readline().split()))

start = 1
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    length = 0

    for i in tree:
        if i >= mid:
            length += i - mid

    if length >= M:
        start = mid + 1
    elif length < M:
        end = mid - 1
        
print(end)