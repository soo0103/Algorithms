import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
requires = list(map(int, sys.stdin.readline().split()))

requires.sort()

left = 0
right = len(requires) - 1
cnt = 0

while left < right:
    armor = requires[left] + requires[right]
    
    if armor == M:
        cnt += 1
        left += 1
    elif armor > M:
        right -= 1
    else:
        left += 1
        
print(cnt)