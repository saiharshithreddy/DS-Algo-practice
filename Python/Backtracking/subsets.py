'''
Approach: BFS

Time complexity: O(2^N)
Space complexity: O(2^N)

Algorithm:
1. Add [] to the subsets
2. Copy elements in subsets and append num to those elements
for ex: step 1 [[]]
        step 2 [[],[1]]
        step 3 [[], [1], [2],[1,2]]
        step 4 [[],[1], [2], [1,2], [3], [1,3], [1,2,3]]
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return

        subsets = []
        subsets.append([])

        for num in nums:
            n = len(subsets)

            for i in range(n):
                # copy subset
                Set = list(subsets[i])
                # add new num to every list of the subset
                Set.append(num)
                # add this to main subsets
                subsets.append(Set)

        return subsets
