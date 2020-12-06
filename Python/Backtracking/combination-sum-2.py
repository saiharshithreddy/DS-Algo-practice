class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(curr, candidates, target):
            if curr:
                target -= curr[-1]
            if target == 0:
                # O(n) search
                if curr not in res:
                    res.append(curr)

            elif target < 0:
                return 0

            for i in range(len(candidates)):
                
                if candidates[i] > target:
                    return
                helper(curr + [candidates[i]], candidates[i+1:], target)
        candidates.sort()
        helper([], candidates, target)
        return res
