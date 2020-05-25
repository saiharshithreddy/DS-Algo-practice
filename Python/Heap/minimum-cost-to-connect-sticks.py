# @Author: Sai Harshith
# @Date:   24-May-2020-13-05
# @Last modified by:   Sai Harshith
# @Last modified time: 24-May-2020-13-05

'''
Greedy: Sticks with min cost have be joined.
Heap is a good data structure to find the min in a changing list of numbers.
TC: O(NlogN)
SC: O(N)
'''
import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        minheap = []
        total_cost = 0
        # Add nums to min heap
        for i in range(len(sticks)):
            heapq.heappush(minheap, sticks[i])
        # extract 2 smallest elements and add their cost
        # push the cost into the minheap
        while len(minheap) > 1:
            cost = heapq.heappop(minheap) + heapq.heappop(minheap)
            total_cost += cost
            heapq.heappush(minheap, cost)
        return total_cost
