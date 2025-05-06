import sys

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        n = int(sys.stdin.readline())

        small = n // 2
        big = n // 2

        while small > 0:
            if is_prime(small) and is_prime(big):
                print(small, big)
                break
            else:
                small -= 1
                big += 1