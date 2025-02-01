import sys

while 1:
    sentence = sys.stdin.readline().rstrip()
    stack = []

    if sentence == '.':
        break

    for i in sentence:
        if i == '[' or  i =='(':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break

    if not stack:
        print("yes")
    else:
        print("no")