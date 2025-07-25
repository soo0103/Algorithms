import sys
import math

N, M, K = map(int, sys.stdin.readline().split())

dot_row = (K - 1) // M + 1
dot_col = K - (dot_row - 1) * M 

down_rows = N - (dot_row - 1)
right_cols = M - (dot_col - 1)

if K == 0:
    total_paths = math.comb(N + M - 2, N - 1)
    
    print(total_paths)
else:
    paths_to_dot = math.comb(dot_row + dot_col - 2, dot_row - 1)
    paths_from_dot = math.comb(down_rows + right_cols - 2, down_rows - 1)

    print(paths_to_dot * paths_from_dot)