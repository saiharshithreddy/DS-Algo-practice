# @Author: Sai Harshith
# @Date:   22-May-2020-13-05
# @Last modified by:   Sai Harshith
# @Last modified time: 22-May-2020-16-05
'''
# sliding window and 2 heaps
# similar to find median in data stream
'''
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = []
        min_heap = []
        res = [0 for i in range(len(nums)-k + 1)]

        # add num to max heap first
        for i in range(len(nums)):

            if not max_heap or -max_heap[0] >= nums[i]:
                heapq.heappush(max_heap, -nums[i])

            else:
                heapq.heappush(min_heap, nums[i])


            # balance the heaps
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, - heapq.heappop(max_heap))
            elif len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

            if i - k + 1 >= 0:
                # both heaps contain equal numbers
                if len(max_heap) == len(min_heap):
                    res[i-k+1] = (-max_heap[0] + min_heap[0]) / 2
                else:
                    res[i-k+1] = -max_heap[0] / 1.0

                # remove the element from the sliding Window
                while max_heap and max_heap[0][1] <= i:
        			heapq.heappop(max_heap)
        		while min_heap and min_heap[0][1] <= i:
        			heapq.heappop(min_heap)
                
