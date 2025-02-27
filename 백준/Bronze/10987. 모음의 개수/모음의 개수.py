import sys

word = sys.stdin.readline().strip()

cnt = 0

for vowel in ('a', 'e', 'i', 'o', 'u'):
    cnt += word.count(vowel)

print(cnt)