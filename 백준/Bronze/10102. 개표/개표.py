import sys

V = int(sys.stdin.readline())

vote = list(map(str, sys.stdin.readline().strip()))

A = vote.count('A')
B = vote.count('B')

if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print("Tie")