import sys

while 1:
    pwd = sys.stdin.readline().rstrip()

    if pwd == "END":
        break

    print(''.join(list(reversed(pwd))))