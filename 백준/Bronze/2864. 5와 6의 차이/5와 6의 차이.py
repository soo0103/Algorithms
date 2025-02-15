import sys

A, B = sys.stdin.readline().split()

minNum = int(A.replace('6', '5')) + int(B.replace('6', '5'))
maxNum = int(A.replace('5', '6')) + int(B.replace('5', '6'))

print(minNum, maxNum)