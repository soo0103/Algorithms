import sys

N = int(sys.stdin.readline())
seq = [int(sys.stdin.readline()) for _ in range(N)]
seq.sort()
used = [False for _ in range(N)]

cnt = 0
result = 0

if N == 1:
    result += seq[0]
else:
    for i in range(N):
        if not used[i]:
            used[i] = True

            if seq[i] < 0:
                if i + 1 < N and seq[i + 1] <= 0:
                    result += seq[i] * seq[i + 1]
                    used[i + 1] = True
                else:
                    result += seq[i]
            elif seq[i] == 0:
                continue
            else:
                if (N - i) % 2 == 0:
                    if N - i != 0:
                        for j in range(i, N, 2):
                            result += max(seq[j] * seq[j + 1], seq[j] + seq[j + 1])
                        break
                else:
                    result += seq[i]
                    
                    if i + 1 < N:
                        for j in range(i + 1, N, 2):
                            result += max(seq[j] * seq[j + 1], seq[j] + seq[j + 1])
                        break

print(result)