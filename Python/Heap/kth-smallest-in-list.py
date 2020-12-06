from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create a max heap
        heapq.heapify(nums)
        largest = heapq.nlargest(k,nums)

        return largest[k-1]

    def findKthSmallest(self, nums: List[int], k: int) -> int:
        # create a max heap
        heapq.heapify(nums)
        smallest = heapq.nsmallest(k,nums)

        return smallest[k-1]
