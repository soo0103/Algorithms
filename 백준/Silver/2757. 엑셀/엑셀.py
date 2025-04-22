import sys

def decimal_to_base26(n):
    if n == 1:
        return 'A'

    result = ''

    while n > 0:
        n -= 1
        result += chr(ord('A') + n % 26)
        n //= 26

    return result[::-1]

if __name__ == "__main__":
    while 1:
        rc = sys.stdin.readline().strip()

        n, m = rc[1:].split('C')

        if n == m == '0':
            break

        m = decimal_to_base26(int(m))

        print(m + n)