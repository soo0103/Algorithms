import sys
from collections import defaultdict

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
integers = list(map(int, sys.stdin.readline().split()))

dic = defaultdict(int)

for card in cards:
    dic[card] = 1

for i in integers:
    if dic[i]:
        print(1, end = " ")
    else:
        print(0, end = " ")