'''
Approach 1: Two pointers
Time complexity: O(n)
Space complexity: O(1)

Algorithm:
1. Check which building height is more and based on it update the respective max height (left/right). 
2. If the current building height is than respective max height (left/right) then add the water count. 

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers 
        left, right = 0, len(height)-1
        left_max, right_max = 0,0
        water_count = 0
        
        while left < right:
            
            # left
            if height[left]< height[right]:
                
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water_count += left_max - height[left]
                    
                left += 1
                
            # right
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water_count += right_max - height[right]
                right -= 1
            
        return water_count