import sys

equation = sys.stdin.readline().strip()

stack = []
result = ''

for eq in equation:
    if eq == '(':
        stack.append(eq)
    elif eq == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    elif eq == '+' or eq == '-':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(eq)
    elif eq == '*' or eq == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            result += stack.pop()
        stack.append(eq)
    else:
        result += eq

while stack:
    result += stack.pop()

print(result)