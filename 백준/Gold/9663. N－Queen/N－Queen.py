import sys

def promising(cnt):
    for i in range(cnt):
        if board[cnt] == board[i] or cnt - i == abs(board[cnt] - board[i]):
            return False
    return True

def nqueen(cnt):
    global value

    if cnt == N:
        value += 1
        return

    for i in range(N):
        board[cnt] = i
        if promising(cnt):
            nqueen(cnt + 1)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    board = [0] * N
    value = 0

    nqueen(0)
    
    print(value)