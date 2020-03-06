'''
Approach: Backtracking
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(2^N)
Space complexity: O(N)

Algorithm:

'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if len(candidates) == 0:
            return
        def func(curr, nums, target):
            if curr:
                target -= curr[-1]
            if target == 0:
                res.append(curr)

            elif target < 0:
                return

            for i in range(len(nums)):
                func(curr + [nums[i]], nums[i:], target)

        func([], candidates, target)
        return res
