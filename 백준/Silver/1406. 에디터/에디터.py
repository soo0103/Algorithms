import sys

s = list(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline())

word = []

for i in range(M):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'L':
        if s:
            word.append(s.pop())
    elif cmd[0] == 'D':
        if word:
            s.append(word.pop())
    elif cmd[0] == 'B':
    	if s:
            s.pop()  
    else:
    	s.append(cmd[1])
        
s.extend(reversed(word))
print(''.join(s))