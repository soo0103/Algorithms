import sys

def is_prime(x):
    if x == 0 or x == 1:
        return False
    
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    
    return True

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        n = int(sys.stdin.readline())

        while 1:
            if is_prime(n):
                print(n)
                break
            else:
                n += 1