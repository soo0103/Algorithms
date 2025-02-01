import sys

A, B = map(int, sys.stdin.readline().split())

seq = []
value = 0

for i in range(46):
    for j in range(i):
        seq.append(i)

for k in range(A - 1, B):
    value += seq[k]

print(value)