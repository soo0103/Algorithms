import sys

N = int(sys.stdin.readline())
cnt = 0

for _ in range(N):
    stack = []
    s = list(sys.stdin.readline().strip())

    for i in range(len(s)):
        if len(stack) > 0:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    if len(stack) == 0:
        cnt += 1
        
print(cnt)