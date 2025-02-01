import sys

N, M = map(int, sys.stdin.readline().split())

nucleotide = {0:'A', 1:'C', 2:'G', 3:'T'}
dna = []
value = []
distance = 0

for i in range(N):
    dna.append(sys.stdin.readline().strip())

for c in range(M):
    comp = [0, 0, 0, 0]

    for r in range(N):
        if dna[r][c] == 'A':
            comp[0] += 1
        elif dna[r][c] == 'C':
            comp[1] += 1
        elif dna[r][c] == 'G':
            comp[2] += 1
        else:
            comp[3] += 1
    
    if comp.count(max(comp)) > 1:
        arr = []
        arr.append(max(comp))
        alp = min(arr)
        value.append(nucleotide[comp.index(alp)])
    else:
        value.append(nucleotide[comp.index(max(comp))])

for r in range(N):
    for c in range(M):
        if dna[r][c] != value[c]:
            distance += 1
        
print(''.join(value))
print(distance)