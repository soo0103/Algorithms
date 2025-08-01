import sys

H, W = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))

left = 0
right = W - 1
left_max = heights[left]
right_max = heights[right]
rain = 0

while left < right:
    if left_max <= right_max:
        left += 1
        left_max = max(left_max, heights[left])
        rain += max(0, left_max - heights[left])
    else:
        right -= 1
        right_max = max(right_max, heights[right])
        rain += max(0, right_max - heights[right])

print(rain)