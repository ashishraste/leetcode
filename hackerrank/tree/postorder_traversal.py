from tree import *

def postOrder(root):
    if root.left != None: postOrder(root.left)
    if root.right != None: postOrder(root.right)
    print(root.info, end=' ')

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

postOrder(tree.root)