import sys

N = int(sys.stdin.readline())

dic = {}
result = 0

for _ in range(N):
    word = sys.stdin.readline().strip()

    for i in range(len(word)):
        if word[i] in dic:
            dic[word[i]] += 10 ** (len(word) - i - 1)
        else:
            dic[word[i]] = 10 ** (len(word) - i - 1)

dic = sorted(dic.items(), key = lambda x: -x[1])

for i in range(len(dic)):
    result += dic[i][1] * (9 - i)

print(result)