import sys

def is_prime(x):
    if x == 1:
        return False
    
    if x == 2:
        return True

    for i in range(2, int(x ** 0.5) + 1):
        if x % i  == 0:
            return False
    
    return True

if __name__ == "__main__":
    M = int(sys.stdin.readline())
    N = int(sys.stdin.readline())

    result = []

    for i in range(M, N + 1):
        if is_prime(i):
            result.append(i)

    if result:
        print(sum(result))    
        print(result[0])
    else:
        print(-1)