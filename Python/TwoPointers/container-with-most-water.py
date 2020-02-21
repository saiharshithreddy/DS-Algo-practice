class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # two pointer approach
        left = 0
        right = len(height)-1
        # area = length x breadth
        max_area = 0
        while(left<right):
            if height[left] > height[right]:

                max_area = max(max_area, height[right]*(right-left))
                right -=1
            else:
                
                max_area = max(max_area, height[left]*(right-left))
                left += 1
            
        return max_area