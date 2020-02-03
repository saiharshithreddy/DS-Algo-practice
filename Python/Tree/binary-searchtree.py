class Node:
    def __init__(self, val):
        self.leftchild = None
        self.val = val
        self.rightchild = None
        self.parent = None
    
    def insert(self, val):
        if val < self.val:
            if self.leftchild:
                self.leftchild.insert(val)
            else:
                self.leftchild = Node(val)
                return 
        else:
            if self.rightchild:
                self.rightchild.insert(val)
            else:
                self.rightchild = Node(val)
                return


class binary_search_tree(self, root):
    def __init__(self,val):
        self.root = Node(val)
