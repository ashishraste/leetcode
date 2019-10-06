from tree import BinarSearchTree

def height(root):
    if not root:
        return 0  
    return 1 + max(height(root.left), height(root.right))

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))