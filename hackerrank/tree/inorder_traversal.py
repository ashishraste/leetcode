from tree import *

def inOrder(root):
    if root.left != None: inOrder(root.left)
    print(root.info, end=' ')    
    if root.right != None: inOrder(root.right)

tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

inOrder(tree.root)