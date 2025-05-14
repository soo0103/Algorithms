import sys

MOD = 1000000007

def get_gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def get_square(x, exp):
    if exp == 1:
        return x
    
    if exp % 2 == 0:
        return (get_square(x, exp // 2) ** 2) % MOD
    else:
        return x * get_square(x, exp - 1) % MOD

def get_expected_value(x, y):
    return (y * get_square(x, MOD - 2)) % MOD 

if __name__ == "__main__":
    M = int(sys.stdin.readline())

    result = 0

    for _ in range(M):
        N, S = map(int, sys.stdin.readline().split())
        
        gcd = get_gcd(N, S)
        N //= gcd
        S //= gcd
        
        result += get_expected_value(N, S)
        result %= MOD
        
    print(result)