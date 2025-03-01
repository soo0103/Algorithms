import sys

X = int(sys.stdin.readline())

stick = 64
cnt = 0

while X > 0:
    if X >= stick:
        X -= stick
        cnt += 1
    
    stick = stick // 2

print(cnt)