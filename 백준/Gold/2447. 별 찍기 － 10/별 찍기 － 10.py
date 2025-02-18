import sys

def recursion(n, arr):
    if n == N:
        return arr
    
    stars = []

    for i in range(n):
        stars.append(arr[i] * 3)
    
    for i in range(n):
        stars.append(arr[i] + ' ' * n + arr[i])
    
    for i in range(n):
        stars.append(arr[i] * 3)

    return recursion(n * 3, stars)

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    start = ["***", "* *", "***"]

    result = recursion(3, start)

    for i in result:
        print(i)