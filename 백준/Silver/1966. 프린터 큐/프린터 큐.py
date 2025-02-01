import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int,(sys.stdin.readline().split()))
    dq = deque(list(map(int,(sys.stdin.readline().split()))))

    if N == 1:
        print(1)
    else:
        cnt = 0

        while dq:
            elem = dq.popleft()
            
            if dq and max(dq) > elem:
                dq.append(elem)
            else:
                cnt += 1

                if M == 0:
                    break

            M = (M - 1) % len(dq)
                               
        print(cnt)