import sys
sys.setrecursionlimit(10 ** 6)

def postorder(start, end):
    if start > end:
        return
    
    mid = end + 1

    for i in range(start + 1, end + 1):
        if preorder[start] < preorder[i]:
            mid = i
            break

    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(preorder[start])

if __name__ == "__main__":
    preorder = []

    while 1:
        try:
            preorder.append(int(sys.stdin.readline()))
        except:
            break

    postorder(0, len(preorder) - 1)