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

'''
Approach: Heap
TC: O(NlogK)
SC:O(N) for dictionary and O(k) for heap 
'''
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for i in range(len(nums)):
            if nums[i] not in num_count:
                num_count[nums[i]] = 1
            else:
                num_count[nums[i]] += 1
        min_heap = []


        for key, val in num_count.items():
            heapq.heappush(min_heap, (val,key))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        return result
