import sys

N, M = map(int, sys.stdin.readline().split())
pokemon = {}

for i in range(1, N + 1):
    s = sys.stdin.readline().rstrip()
    pokemon[s] = i
    pokemon[i] = s

for j in range(M):
    name = sys.stdin.readline().rstrip()

    if name.isalpha():
        print(pokemon[name])
        
    elif name.isdigit():
        print(pokemon[int(name)])