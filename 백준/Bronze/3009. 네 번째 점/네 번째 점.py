import sys

dicX = {}
dicY = {}

for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())

    if x in dicX:
        dicX[x] += 1
    else:
        dicX[x] = 1

    if y in dicY:
        dicY[y] += 1
    else:
        dicY[y] = 1
    
print(min(dicX, key = dicX.get) , min(dicY, key = dicY.get))