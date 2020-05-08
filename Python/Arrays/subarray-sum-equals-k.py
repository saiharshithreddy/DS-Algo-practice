'''

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_count = {}
        sum_count[0] = 1
        count = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum-k in sum_count:
                count += sum_count[sum-k]
            if sum not in sum_count:
                sum_count[sum] = 1
            else:
                sum_count[sum] += 1
            
        return count
        