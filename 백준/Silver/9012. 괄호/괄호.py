import sys

T = int(sys.stdin.readline())

for _ in range(T):
    stack = []
    s = sys.stdin.readline().strip()

    for j in s:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append(')')
                break
    
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")