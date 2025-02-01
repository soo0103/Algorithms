import sys

N, K = map(int, sys.stdin.readline().split())
arr = []
point = 0
cnt = 0
flag = True

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

while 1:
    point = arr[point]
    cnt += 1

    if point == K:
        break

    if cnt > N or point == arr[point]:
        flag = False
        break
    
if flag:
    print(cnt)
else:
    print(-1)