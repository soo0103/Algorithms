import sys

def binary_search(arr, x):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return start

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    lis = []

    for i in range(N):
        if not lis or A[i] > lis[-1]:
            lis.append(A[i])
        else:
            index = binary_search(lis, A[i])
            lis[index] = A[i]
            
    print(len(lis))