import sys
from collections import defaultdict

nums = defaultdict(int)

N = sys.stdin.readline().strip()

for i in N:
    if int(i) == 6 or int(i) == 9:
        if nums[6] <= nums[9]:
            nums[6] += 1
        else:
            nums[9] += 1
    else:
        nums[int(i)] += 1

nums = sorted(nums.items(), key = lambda x: -x[1])

print(nums[0][1])