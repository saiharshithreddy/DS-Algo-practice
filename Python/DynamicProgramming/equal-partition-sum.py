class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = sum(nums)

        if sum % 2 != 0:
            return False

        dp = [-1]
