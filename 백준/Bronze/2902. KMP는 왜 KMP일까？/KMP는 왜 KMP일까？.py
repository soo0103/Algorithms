import sys

words = list(sys.stdin.readline().split('-'))

KMP = ''

for word in words:
    KMP += word[0]

print(KMP)