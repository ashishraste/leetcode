from tree import *

def preOrder(root):    
    print(root.info, end=' ')
    if root.left != None: preOrder(root.left)
    if root.right != None: preOrder(root.right)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)