import sys

def divide_and_conquer(n, arr):
    temp = 0
    
    for i in arr:
        temp += sum(i)
    
    if temp == n ** 2:
        return '1'
    if temp == 0:
        return '0'
    
    half = n // 2
    top_left     = [row[:half] for row in arr[:half]]
    top_right    = [row[half:] for row in arr[:half]]
    bottom_left  = [row[:half] for row in arr[half:]]
    bottom_right = [row[half:] for row in arr[half:]]
    
    result = '('
    result += divide_and_conquer(half, top_left)
    result += divide_and_conquer(half, top_right)
    result += divide_and_conquer(half, bottom_left)
    result += divide_and_conquer(half, bottom_right)
    result += ')'
    
    return result

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    image = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

    print(divide_and_conquer(N, image))