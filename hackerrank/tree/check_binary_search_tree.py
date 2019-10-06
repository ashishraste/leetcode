from tree import Node

def check_binary_search_tree_(root):
    def check_binary_search_tree(root, min_val=-1, max_val=10**4 + 1):
        if not root: return True       
        val = root.data     
        if val <= min_val or val >= max_val:
            return False
        
        if not check_binary_search_tree(root.right, val, max_val):
            return False
        
        if not check_binary_search_tree(root.left, min_val, val):
            return False
        
        return True
        
    return check_binary_search_tree(root)