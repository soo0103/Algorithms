import sys

S = sys.stdin.readline().strip()

stack  = []
answer = ''
tmp = ''
flag = False

for i in S:
    if i == '<':
        flag = True

        for _ in range(len(stack)):
            answer += stack.pop()
    
    stack.append(i)

    if i == '>':
        flag = False
        
        for _ in range(len(stack)):
            tmp += stack.pop()
        
        answer += tmp[::-1]
        tmp = ''

    if i == ' ' and not flag:
        for j in range(len(stack)):
            if j == 0:
                stack.pop()
                continue

            answer += stack.pop()
        answer += ' '

if stack:
    for _ in range(len(stack)):
        answer += stack.pop()

print(answer)