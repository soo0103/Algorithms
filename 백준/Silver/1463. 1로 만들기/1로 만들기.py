import sys

def operate(X):
    for i in range(2, X + 1):
        op[i] = op[i - 1] + 1

        if i % 2 == 0:
            op[i] = min(op[i], op[i // 2] + 1)
        
        if i % 3 == 0:
            op[i] = min(op[i], op[i // 3] + 1)
            
    return

if __name__ == "__main__":
    X = int(sys.stdin.readline())
    op = [0] * (X + 1)
    
    operate(X)

    print(op[X])