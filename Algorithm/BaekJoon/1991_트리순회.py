import sys
input = sys.stdin.readline

# 전위 순회
def preorder(root):
    print(chr(root + 65), end='')

    if tree[root][0] != -19:
        preorder(tree[root][0])
        
    if tree[root][1] != -19:
        preorder(tree[root][1])

# 중위 순회
def inorder(root):
    if tree[root][0] != -19:
        inorder(tree[root][0])

    print(chr(root + 65), end='')
        
    if tree[root][1] != -19:
        inorder(tree[root][1])

# 후위 순회
def postorder(root):
    if tree[root][0] != -19:
        postorder(tree[root][0])

    if tree[root][1] != -19:
        postorder(tree[root][1])

    print(chr(root + 65), end='')


'''main'''
N = int(input())
tree = [[] for _ in range(26)]

for _ in range(N):
    root, left, right = input().split()

    # '.' = -19
    tree[ord(root) - 65].append(ord(left) - 65)
    tree[ord(root) - 65].append(ord(right) - 65)

preorder(0)
print()
inorder(0)
print()
postorder(0)