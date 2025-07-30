import sys

S = sys.stdin.readline().strip()

stack = []
value = 1
result = 0

for i in range(len(S)):
    c = S[i]
    if c == '(':
        value *= 2
        stack.append(c)
    elif c == '[':
        value *= 3
        stack.append((c))
    elif c == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if S[i - 1] == '(':
            result += value
        value //= 2
        stack.pop()
    elif c == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if S[i - 1] == '[':
            result += value
        value //= 3
        stack.pop()

if not stack:
    print(result)
else:
    print(0)