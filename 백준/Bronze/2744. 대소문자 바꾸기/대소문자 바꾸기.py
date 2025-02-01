import sys

word = list(map(str, sys.stdin.readline()))

for i in word:
    if i.islower():
        print(i.upper(), end = '')
    elif i.isupper():
        print(i.lower(), end = '')