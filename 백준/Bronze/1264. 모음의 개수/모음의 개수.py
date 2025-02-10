import sys

while 1:
    sentence = sys.stdin.readline().rstrip()
    cnt = 0

    if sentence == '#':
        break

    for i in ('a', 'e', 'i', 'o', 'u'):
        cnt += sentence.lower().count(i)

    print(cnt)