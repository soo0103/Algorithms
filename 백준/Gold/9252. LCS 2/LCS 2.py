import sys

seq1 = ' ' + sys.stdin.readline().rstrip()
seq2 = ' ' + sys.stdin.readline().rstrip()

len1 = len(seq1)
len2 = len(seq2)
dp = [[''] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if seq1[i - 1] == seq2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + seq1[i - 1]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(len(dp[-1][-1]) - 1)
print(dp[-1][-1].strip())