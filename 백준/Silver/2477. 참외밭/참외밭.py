import sys

K = int(sys.stdin.readline())

height = []
width = []
field = []

for _ in range(6):
    direction, length = map(int, sys.stdin.readline().split())
    
    if direction == 1 or direction == 2:
        width.append(length)
    else:
        height.append(length)
    
    field.append((direction, length))

rect1 = max(height) * max(width)

for i in range(6):
    if field[i - 1][0] == 1 and field[(i + 1) % 6][0] == 1:
        if field[i][0] == 3:
            rect2 = field[i - 1][1] * field[i][1]
        elif field[i][0] == 4:
            rect2 = field[i][1] * field[(i + 1) % 6][1]
    elif field[i - 1][0] == 2 and field[(i + 1) % 6][0] == 2:
        if field[i][0] == 3:
            rect2 = field[i][1] * field[(i + 1) % 6][1]
        elif field[i][0] == 4:
            rect2 = field[i - 1][1] * field[i][1]

print((rect1 - rect2) * K)