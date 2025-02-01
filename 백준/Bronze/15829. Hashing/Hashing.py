import sys

L = int(sys.stdin.readline())
sentence = sys.stdin.readline().strip()
r = 31
M = 1234567891
H = 0

for i in range(L):
    H += ((ord(sentence[i]) - 96) * (r ** i))

print(H % M)