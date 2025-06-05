import sys

S = list(map(int, str(sys.stdin.readline().strip())))

length = 0

for i in range(2, len(S) + 1, 2):
    for j in range(len(S) - i + 1):
        if sum(S[j:j + i // 2]) == sum(S[j + i // 2:j + i]):
            length = max(length, i)
    
print(length)