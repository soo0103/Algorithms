import sys

word = sys.stdin.readline().strip()

l = len(word) // 10

for i in range(l):
    print(word[10 * i:10 * (i + 1)])

if len(word) % 10 != 0:
    print(word[l * 10:])