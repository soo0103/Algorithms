import sys

N = int(sys.stdin.readline())

direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]

points = set()

for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    
    lines = [d]
    points.add((y, x))
    
    for gen in range(g):
        dragon_curve = []
        
        for line in lines:
            new_line = (line + 1) % 4
            dragon_curve.append(new_line)
        
        for curve in dragon_curve[::-1]:
            lines.append(curve)
    
    ny = y
    nx = x
    
    for line in lines:
        dy, dx = direction[line]
        ny += dy
        nx += dx
        points.add((ny, nx))
        
sides = [(0, 1), (1, 0), (1, 1)]
cnt = 0

for point in points:
    y, x = point
    flag = True
    
    for side in sides:
        dy, dx = side
        ny = y + dy
        nx = x + dx
        
        if (ny, nx) not in points:
            flag = False
            break
        
    if flag:
        cnt += 1
            
print(cnt)