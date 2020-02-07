def findAncestors(root,k):
    result = []
    helper(root,k,result)

    def helper(root,k, result):

        
        if root is None:
            return False

        elif root.val == k:
            return True

        elif helper(root.left, k, result) or helper(root.right, k , result):
            result.append(root.val)
            return True

        return False
