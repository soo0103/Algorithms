import sys

X = int(sys.stdin.readline())

line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line - X + 1

elif line % 2 == 1:
    a = line - X + 1
    b = X
    
print(f'{a}/{b}')