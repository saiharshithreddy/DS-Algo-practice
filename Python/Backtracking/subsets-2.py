
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        subsets.append([])
        start , end = 0, 0
        for i in range(len(nums)):

            start = 0
            # to handle duplicates
            if i > 0 and nums[i] == nums[i-1]:
                start = end + 1
            end = len(subsets)-1
            # if prev num and curr num are equal then subsets created in the previous step are copied and nums are               #    added to them.
            for j in range(start, end+1):
                Set = list(subsets[j])
                Set.append(nums[i])
                subsets.append(Set)

        return subsets
