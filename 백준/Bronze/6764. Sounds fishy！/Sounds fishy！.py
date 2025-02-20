import sys

depth = [int(sys.stdin.readline()) for _ in range(4)]

if len(set(depth)) == 1: 
    print("Fish At Constant Depth")
elif sorted(depth) == depth:
    if len(set(depth)) != len(depth):
        print("No Fish")
    else:
        print("Fish Rising")
elif sorted(depth, reverse = True) == depth:
    if len(set(depth)) != len(depth):
        print("No Fish")
    else:
        print("Fish Diving")
else:
    print("No Fish")