import sys
from itertools import permutations

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split())) 
result = 0

for i in permutations(seq):
  value = 0

  for j in range(N - 1):
    value += abs(i[j] - i[j + 1])

  result = max(result, value)

print(result)