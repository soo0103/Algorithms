import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    max_heap = []
    min_heap = []
    items = {}
     
    k = int(sys.stdin.readline())
    
    for _ in range(k):
        op, num = sys.stdin.readline().split()
        num = int(num)
        
        if op == 'I':
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
            if num in items:
                items[num] += 1
            else:
                items[num] = 1
            
        elif op == 'D':
            if num == 1:
                while max_heap and items[-max_heap[0]] < 1:
                    heapq.heappop(max_heap)
                if max_heap and items[-max_heap[0]] >= 1:
                    items[-max_heap[0]] -= 1
                    heapq.heappop(max_heap)
                
            elif num == -1:
                while min_heap and items[min_heap[0]] < 1:
                    heapq.heappop(min_heap)
                if min_heap and items[min_heap[0]] >= 1:
                    items[min_heap[0]] -= 1
                    heapq.heappop(min_heap)
    
    while max_heap and items[-max_heap[0]] < 1:
        heapq.heappop(max_heap)
                    
    while min_heap and items[min_heap[0]] < 1:
        heapq.heappop(min_heap)
                
    if not max_heap or not min_heap:
        print("EMPTY")
    else: 
        print(-heapq.heappop(max_heap), heapq.heappop(min_heap))