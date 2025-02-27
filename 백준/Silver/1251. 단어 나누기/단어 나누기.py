import sys

word = list(sys.stdin.readline().strip())

words = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        a = word[:i][::-1]
        b = word[i:j][::-1]
        c = word[j:][::-1]

        words.append(a + b + c)
        
words.sort()

print(*words[0], sep = '')