import sys

def seq(pre):
    prev = pre
    
    if len(s) == M:
        sequence.append((tuple(s)))
        return

    for i in range(N):
        if arr[i] >= prev:
            s.append(arr[i])
            prev = arr[i]
            seq(prev)
            s.pop()

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    s = []
    sequence = []
    
    seq(0)
    
    sequence = sorted(set(sequence))
    
    for i in range(len(sequence)):
        print(*sequence[i])