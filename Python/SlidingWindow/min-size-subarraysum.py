class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        start = 0
        arr_sum = 0
        min_size = float('inf')
        for end in range(len(nums)):
            arr_sum += nums[end]

            while arr_sum >= s:
                min_size = min(min_size, (end-start+1))
                arr_sum -= nums[start]
                start += 1
        return min_size if min_size != float('inf') else 0
            
