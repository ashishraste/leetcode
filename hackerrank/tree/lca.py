from tree import BinarySearchTree

lca_root = None

def lca(root, v1, v2):
    global lca_root
    print(root.info)
    lca_root = root

    # Current root node is higher than both values; traverse left subtree
    if root.info > v1 and root.info > v2:
        lca(root.left, v1, v2)
        
    # Current root node is lower than both values; traverse right subtree    
    if root.info < v1 and root.info < v2:
        lca(root.right, v1, v2)
    
    return lca_root

if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    v = list(map(int, input().split()))

    ans = lca(tree.root, v[0], v[1])
    print(ans.info)