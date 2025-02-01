import sys

n = int(sys.stdin.readline())

stack = []
op = []
now = 1
flag = True

for i in range(n):
    num = int(sys.stdin.readline())
    
    while now <= num:
        stack.append(now)
        op.append('+')
        now += 1

    if num == stack[-1]:
        stack.pop()
        op.append('-')
    
    else:
        flag = False
        break

if not flag:
    print("NO")
else:
    print(*op, sep="\n")