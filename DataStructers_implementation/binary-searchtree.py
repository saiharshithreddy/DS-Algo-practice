class Node:
    def __init__(self, val):
        self.leftchild = None
        self.val = val
        self.rightchild = None
        
    
    def insert(self, val):

        '''
        Recursive approach
        '''
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

        '''
        Iterative approach
        '''
        current = self
        parent = None
        # traversal to left leaf node
        while current:
            parent = current
            if val < current.val:
                # move current to left child
                current = current.leftchild
            else:
                # move current to right child
                current = current.rightchild
        
        # insertion
        if parent == None:
            parent = Node(val)
        elif val < parent.val:
            parent.leftchild = Node(val)

        else:
            parent.rightchild = Node(val)
    
    def search(self,val):
        '''
        Iterative
        '''
        current = self

        while current != None:
            if val < current.val:
                current = current.leftchild
            elif val > current.val:
                current = current.rightchild
            else:
                return True

        return False


        '''
        Recursive
        '''
        if val < self.val:
            if self.leftchild:
                return self.leftchild.search(val)
            else:
                return False
        elif val > self.val:
            if self.rightchild:
                return self.rightchild.search(val)
            else:
                return False
        else:
            return True
        return False

    def delete(self,val):

        if val < self.val:
            if self.leftchild:
                self.leftchild = self.leftchild.delete(val)
            else:
                print("Not in the tree")
        elif val > self.val:
            if self.rightchild:
                self.rightchild = self.rightchild.delete(val)
            else:
                print("Not in the tree")
        else:
            # 1. Delete a leaf node
            if self.leftchild is None and self.rightchild is None:
            # Delete a node with one child
            # Delete a node with two childs
        



class binary_search_tree(self, root):
    def __init__(self,val):
        self.root = Node(val)

    def insert(self,val):
        if self.root:
            self.root.insert(val)
        else:
            self.root = Node(val)
            return True

    def search(self,val):
        if self.root:
            return self.root.search(val)
        else:
            return False

    def delete(self, val):
        if self.root:
            return self.root.delete(val)
        else:
            return False
