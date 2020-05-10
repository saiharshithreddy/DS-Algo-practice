'''
Approach: Sliding window 
similar to 
1. longest repeating character replacement
TC: O(N)
SC: O(1)
'''


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        win_start = 0
        max_length = 0
        
        num_zeros = 0
        
        for win_end in range(len(A)):
            
            if A[win_end] == 0:
                num_zeros += 1
            
            # when 0s are > k in the subarray, check if the starting ele = 0 and decrement the zeros count. 
            while num_zeros > K:
            
                if A[win_start] == 0:
                    num_zeros -= 1
                    
                win_start += 1
            
            # Max of length of the arrays with 0 to k zeros is calculated.   
            max_length = max(max_length, win_end - win_start + 1)
        return max_length