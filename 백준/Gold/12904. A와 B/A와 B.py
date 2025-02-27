import sys

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

flag = True

while S != T:
    if len(T) == 0:
        flag = False
        break
    
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[::-1]
        T = T[1:]
    else:
        flag = False

if flag:
    print(1)
else:
    print(0)