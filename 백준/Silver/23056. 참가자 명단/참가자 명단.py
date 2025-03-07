import sys

N, M = map(int, sys.stdin.readline().split())

participants = []
classes = [0] * (N + 1)

while 1:
    participant = list(sys.stdin.readline().split())

    if participant == ['0', '0']:
        break

    if classes[int(participant[0])] < M:
        classes[int(participant[0])] += 1
    else:
        continue

    participants.append(participant)

participants.sort(key = lambda x: (int(x[0]) % 2 == 0, int(x[0]), len(x[1]), x[1]))

for num, name in participants:
    print(num, name)