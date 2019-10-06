class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info)

class BinaryTree:
    def __init__(self):
        self.root = None        

    def insertElements(self, arr, root, i, n):        
        # Base case for recursion  
        if i < n:
            temp = Node(arr[i])
            root = temp

            # insert left child  
            root.left = self.insertElements(arr, root.left, 
                                        2 * i + 1, n) 
    
            # insert right child  
            root.right = self.insertElements(arr, root.right, 
                                        2 * i + 2, n)
        self.root = root
        return root
                

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
