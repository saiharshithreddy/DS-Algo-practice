'''
Approach: Sliding window without hashmap

We dont need a hashmap as we dont need to know which number to remove as window slides. 
We have to know if the number is odd or not thats all

TC: O(N + k) +k because we move inside the sliding window
SC: O(1)
'''
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        
        win_start = 0
        nice_subarrays = 0
        odd_count = 0

        for win_end in range(len(nums)):
            right_num = nums[win_end]

            # odd number condition
            if right_num %2 != 0:
                odd_count += 1
            
            # Nice subarray means k odd numbers
            if odd_count == k:
                nice_subarrays += 1
            
            # If 
            while win_start < win_end and odd_count > k:
                
                if nums[win_start] % 2 != 0:
                    odd_count -= 1
                    nice_subarrays += 1
                # shrink the window 
                win_start += 1
                
            # [2,2,2,1,1] has 2 odd numbers likewise [2,2,1,1] and [2,1,1] 
            # move the temporary win_start and check for odd count 
            # We dont shrink the main window because after [2,2,2,1,1] there might be [2,2,2,1,1,4] which is also a nice subarray
            i = win_start
            while odd_count == k and i < win_end and nums[i] % 2 == 0:
                nice_subarrays += 1
                i += 1
                
            

        return nice_subarrays





