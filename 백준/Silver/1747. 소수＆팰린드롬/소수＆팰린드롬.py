import sys

def is_palindrome(x):
    x = str(x)
    len_x = len(x) // 2

    if x[:len_x] == x[-1:-len_x - 1:-1]:
        return True
    else:
        return False

def is_prime(x):
    if x < 2:
        return False
    
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    
    return True

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    while 1:
        if is_prime(N) and is_palindrome(N):
            print(N)
            break
        else:
            N += 1