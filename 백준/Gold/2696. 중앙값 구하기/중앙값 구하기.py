import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    M = int(sys.stdin.readline())
    
    arr = []
    for _ in range(M // 10 + 1):
        arr += list(map(int, sys.stdin.readline().split()))
        
    left = []
    right = []
    mid = arr[0]
    seq = [mid]
    
    for i, num in enumerate(arr[1:], 2):
        if num < mid:
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)
        
        if i % 2 == 1:
            if len(left) > len(right):
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)

            if len(left) < len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)

            seq.append(mid)
    
    print(len(seq))
    
    for i in range(len(seq)):
        if i != 0 and i % 10 == 0:
            print()
        print(seq[i], end=' ')
    print()