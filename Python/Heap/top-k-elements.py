'''
Approach: Using dictionary
Difficulties faced: None
Steps to resolve Difficulties:
Time complexity: O(NlogN)
Space complexity: O(N)
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict = {}
        # O(N)
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
        # O(NlogN)
        li = sorted(dict.items(), key =
             lambda kv:( kv[1],kv[0]))

        result = [x[0] for x in li]

        return result[-k:]