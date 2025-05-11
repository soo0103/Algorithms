import sys

N, K = map(int, sys.stdin.readline().split())
temperature = list(map(int, sys.stdin.readline().split()))

comp = sum(temperature[0:K])
max_temperature = comp

for i in range(N - K):
    comp += temperature[i + K] - temperature[i]
    
    if comp > max_temperature:
        max_temperature = comp

print(max_temperature)