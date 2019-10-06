from tree import BinarySearchTree

nodes = []
def inorder(root):
    global nodes
    if root.left != None: inorder(root.left)
    nodes.append(root.info)        
    if root.right != None: inorder(root.right)

def test_inorder():
    inorder_nodes = [0,2,3,4,5,6,7,8,9]
    arr_elements = [6,2,8,0,4,7,9,3,5]
    tree = BinarySearchTree()
    for i in range(len(arr_elements)):
        tree.create(arr_elements[i])

    inorder(tree.root)

    for i in range(len(inorder_nodes)):
        assert inorder_nodes[i] == nodes[i]