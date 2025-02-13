import sys

N = list(map(int, sys.stdin.readline().split()))

flag = False

if len(N) == 1:
    flag = True
else:
    for i in range(len(N) - 1):
        if N[i] > N[i + 1]:
            flag = False
            break
        else:
            flag = True

if flag:
    print("Good")
else:
    print("Bad")