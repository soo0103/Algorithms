import sys
from collections import defaultdict

word = sys.stdin.readline().strip()

dic = defaultdict(int)

for i in word:
    dic[i] += 1

for c in "abcdefghijklmnopqrstuvwxyz":
    print(dic[c], end = ' ')