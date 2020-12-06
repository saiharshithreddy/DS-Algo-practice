class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hashmap O(N) space

        # O(N) and O(1)
        # bit manipulation
        # XOR
        a = 0
        for i in nums:
            a ^= i
        return a
        
