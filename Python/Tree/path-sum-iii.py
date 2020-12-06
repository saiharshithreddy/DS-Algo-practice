# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        def dfs(node, path_sum):
            if not node:
                return
            path_sum += node.val
            if path_sum == sum: self.count +=1
                
            if path_sum - sum in hashmap:
                self.count += hashmap[path_sum - sum]
            if path_sum not in hashmap:
                hashmap[path_sum] = 1
            else:
                hashmap[path_sum] += 1
            
            
            dfs(node.left, path_sum)
            
            dfs(node.right, path_sum)
            # if we first move to left side and come back to right side, left side subarray sums shouldn't be there in right side, so backtracking lookup.
            hashmap[path_sum] -= 1
        
        hashmap = {}
        path_sum = 0
        self.count = 0
        
        dfs(root, path_sum)
        return self.count
    