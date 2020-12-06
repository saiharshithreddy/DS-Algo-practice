class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1,10))

        res = []
        def helper(curr, nums, n):
            if curr:
                n -= curr[-1]

            if n == 0:
                if curr not in res and len(curr) == k:
                    res.append(curr)
            if n < 0:
                return

            for i in range(len(nums)):
                if nums[i] > n:
                    return
                helper(curr + [nums[i]], nums[i+1:], n)

        helper([], nums, n)
        return res

        
