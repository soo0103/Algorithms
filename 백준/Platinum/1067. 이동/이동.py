import sys

MOD = 998244353 # A sufficiently large prime, of the form 2^k * c + 1
PRIMITIVE_ROOT = 3 # Primitive root modulo MOD

def fft(arr, is_inverse):
    n = len(arr)
    bit_reversed_index = 0
    
    # Bit-Reversal Permutation
    for current_index in range(1, n):
        half = n // 2
        
        while bit_reversed_index >= half:
            bit_reversed_index -= half
            half //= 2
        
        bit_reversed_index += half

        if current_index < bit_reversed_index:
            arr[current_index], arr[bit_reversed_index] = arr[bit_reversed_index], arr[current_index]
    
    # Cooley-Tukey FFT
    block_size = 2

    while block_size <= n:
        half_block = block_size // 2
        root = pow(PRIMITIVE_ROOT, MOD // block_size, MOD) # Unit root (root of unity)
    
        if is_inverse:
            root = pow(root, MOD - 2, MOD) # Use modular inverse for inverse FFT
        
        for start in range(0, n, block_size):
            omega = 1 # Start with w^0

            for i in range(start, start + half_block):
                even = arr[i]
                odd = arr[i + half_block] * omega
                arr[i] = (even + odd) % MOD
                arr[i + half_block] = (even - odd) % MOD
                omega = (omega * root) % MOD

        block_size *= 2

    # Normalization step for inverse FFT
    if is_inverse:
        inverse_n = pow(n, MOD - 2, MOD)  # Modular inverse of n
        
        for i in range(n):
            arr[i] = (arr[i] * inverse_n) % MOD

def convolution(x, y):
    length = len(x) + len(y) - 1
    n = 1 << length.bit_length()

    x += [0] * (n - len(x))
    y += [0] * (n - len(y))

    fft(x, False)
    fft(y, False)

    for i in range(n):
        x[i] *= y[i]
    
    fft(x, True)

    return x

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    X = list(map(int, sys.stdin.readline().split()))
    Y = list(map(int, sys.stdin.readline().split()))

    Y.reverse()
    result = convolution(X + X, Y)

    print(max(result))