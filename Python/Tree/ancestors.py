# @Author: Sai Harshith
# @Date:   05-Feb-2020-22-02
# @Last modified by:   Sai Harshith
# @Last modified time: 11-Jun-2020-00-06



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
