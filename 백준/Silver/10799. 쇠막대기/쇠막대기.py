import sys

laser = sys.stdin.readline().strip()

stick = 0
stack = []

for i in range(len(laser)):
    if laser[i] == '(':
        stack.append('(')

    elif laser[i] == ')':
        if laser[i - 1] == '(':
            stack.pop()
            stick += len(stack)
        else:
            stack.pop()
            stick += 1

print(stick)