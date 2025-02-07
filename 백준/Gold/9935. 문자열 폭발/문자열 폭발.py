import sys

word = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

stack = []
l = len(bomb)

for i in range(len(word)):
    stack.append(word[i])

    if ''.join(stack[-l:]) == bomb:
        for _ in range(l):
            stack.pop()

if stack:
    print(*stack, sep='')
else:
    print("FRULA")