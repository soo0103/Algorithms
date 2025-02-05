import sys

i = 1

while 1:
    a, b, c = map(int, sys.stdin.readline().split())

    if a == b == c == 0:
        break

    print(f"Triangle #{i}")

    if c == -1:
        print(f"c = {(a ** 2 + b ** 2) ** 0.5:.3f}")
    else:
        if a == -1:
            if (c ** 2 - b ** 2) > 0:
                print(f"a = {(c ** 2 - b ** 2) ** 0.5:.3f}")
            else:
                print("Impossible.")
        elif b == -1:
            if (c ** 2 - a ** 2) > 0:
                print(f"b = {(c ** 2 - a ** 2) ** 0.5:.3f}")
            else:
                print("Impossible.")
    
    print()
    i += 1