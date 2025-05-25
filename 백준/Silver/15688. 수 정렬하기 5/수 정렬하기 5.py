import sys

N = int(sys.stdin.readline())
nums = list(int(sys.stdin.readline()) for _ in range(N))

nums.sort()

for num in nums:
    print(num)