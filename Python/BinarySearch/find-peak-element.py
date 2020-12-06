'''
Peak element: nums[i-1] < nums[i] > nums[i+1]
Approach: Binary search

nums = [1,2,3,9,4,5,0]

peak = 5 
l      m      h
[1,2,3,9,4,5,0]

if nums[mid] < nums[mid+1]:  9 < 4 false
TC: O(logN)
SC: O(1)
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid
                
        return low
        