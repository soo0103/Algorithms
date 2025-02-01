import sys

def preorder(now):
    if now != '.':
        print(now, end='')
        preorder(tree[now][0])
        preorder(tree[now][1])
    
def inorder(now):
    if now != '.':
        inorder(tree[now][0])
        print(now, end='')
        inorder(tree[now][1])

def postorder(now):
    if now != '.':
        postorder(tree[now][0])
        postorder(tree[now][1])
        print(now, end='')

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    tree = {}

    for _ in range(N):
        node, left, right = sys.stdin.readline().split()
        tree[node] = (left, right)

    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')