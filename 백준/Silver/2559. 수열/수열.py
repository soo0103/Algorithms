import sys

N, K = map(int, sys.stdin.readline().split())
temperature = list(map(int, sys.stdin.readline().split()))

left = 0
right = K - 1
comp = sum(temperature[left:right + 1])
max_temperature = comp

while right < len(temperature) - 1:
    right += 1
    comp = comp - temperature[left] + temperature[right]
    left += 1
    
    if comp > max_temperature:
        max_temperature = comp

print(max_temperature)