'''
1. Monotonically decreasing stack
2. Hashmap to store (num, next_greater element) 
TC: O(m+n) m: len(nums1) n: len(nums2)
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # monotonically decreasing stack
        
        # hashmap to store (num, next greatest num)
        
        num_map = {}
        stack = []
        res = []
        
        for i in range(len(nums2)):
            while len(stack) and stack[-1] < nums2[i]:
                num_map[stack.pop()] = nums2[i]
                
            stack.append(nums2[i])
            
        for i in range(len(nums1)):
            res.append(num_map.get(nums1[i], -1))
        
        return res