import sys

while 1:
    x, y = map(float, sys.stdin.readline().split())

    if x == 0 or y == 0:
        print("AXIS")
        
        if x == 0 and y == 0:
            break

    if x > 0:
        if y > 0:
            print("Q1")
        elif y < 0:
            print("Q4")
    elif x < 0:
        if y > 0:
            print("Q2")
        elif y < 0:
            print("Q3")