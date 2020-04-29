'''
**Algorithm**

1. Inorder contains root of the tree at first index. Pop it and create a node
2. Slice the the preorder list into two parts  i.e left subtree list (inorder[:inorder.index(root)]) and right subtree list (inorder[inorder.index(root)+1:])
3. In each subtree to get the root, check inorder list

'''

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        # get the root
        root_val = preorder.pop(0)  # O(N)
        # create a node
        root = TreeNode(root_val)

        inorderIndex = inorder.index(root_val)  # O(N)

        root.left = self.buildTree(preorder, inorder[:inorderIndex])  # O(N)
        root.right = self.buildTree(preorder, inorder[inorderIndex+1:])  # O(N)
        return root
