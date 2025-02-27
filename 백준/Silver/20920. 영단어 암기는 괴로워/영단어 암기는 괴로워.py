import sys

words = {}

N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    word = sys.stdin.readline().strip()

    if len(word) >= M:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

words = sorted(words.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in range(len(words)):
    print(words[i][0])