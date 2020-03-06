# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        def helper(root):
            # base case
            if not root:
                res.append(None)
                return
            else:
                res.append(root.val)
 
            # recursive call
            helper(root.left)
            helper(root.right)
        
        helper(root)
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        res = data.strip('][').split(', ')
        
        def rec(res):
            # base case
            if res[0] == 'None':
                res.pop(0)
                return None
            
            node = TreeNode(res[0])
            res.pop(0)
            node.left = rec(res)
            node.right = rec(res)
            return node
           
        
        root = rec(res)
        return root
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))