from tree import BinarySearchTree
from lca import lca
def test_lca():
    arr_elements = [6,2,8,0,4,7,9,3,5]
    tree = BinarySearchTree()
    for i in range(len(arr_elements)):
        tree.create(arr_elements[i])
    
    lca_node = lca(tree.root, 2, 8)
    assert lca_node.info == 6

    lca_node = lca(tree.root, 2, 4)
    assert lca_node.info == 2
