import sys

def get_primes(N):
    result = []

    for i in range(2, N + 1):
        if arr[i]:
            result.append(i)
            
            for j in range(2 * i, N + 1, i):
                arr[j] = False
    
    return result

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    arr = [False, False] + [True] * (N - 1)

    primes = get_primes(N)

    left = 0
    right = 0
    cnt = 0

    while right < len(primes):
        sum_primes = sum(primes[left:right + 1])

        if sum_primes == N:
            cnt += 1
            right += 1
        elif sum_primes < N:
            right += 1
        else:
            left += 1

    print(cnt)