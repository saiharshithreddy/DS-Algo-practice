'''
Approach: Sliding window 
idea same as #1248 count-number-of-nice-subarrays
'''

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        win_start = 0
        count = 0
        sum = 0
        for win_end in range(len(A)):
            right_num = A[win_end]
            sum += right_num
            
            if sum == S:
                count += 1
                
            while win_start < win_end and sum > S:
                left_num = A[win_start]
                sum -= left_num
                if sum == S:
                    count += 1
                win_start += 1
            
            i = win_start
            while sum == S and i < win_end and A[i] == 0:
                count += 1  
                i += 1
                
        return count
        


'''
Concise sliding window using atmostK concept
'''

def numSubarraysWithSum(self, A, S):
        def atMost(S):
            if S < 0: return 0
            res = i = 0
            for j in range(len(A)):
                S -= A[j]
                while S < 0:
                    S += A[i]
                    i += 1
                # reduces the computation
                res += j - i + 1
            return res
        return atMost(S) - atMost(S - 1)