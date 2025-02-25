import sys

seq = sys.stdin.readline().strip()

result = 10

for i in range(1, len(seq)):
    if seq[i] == seq[i - 1]:
        result += 5
    else:
        result += 10

print(result)