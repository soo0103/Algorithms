import sys

numbers = list(range(1, 10001))
nums = []

for i in range(1, 10001):
    num = i

    for j in str(i):
        num += int(j)

    nums.append(num)

result = [x for x in numbers if x not in nums]

for i in result:
    print(i)