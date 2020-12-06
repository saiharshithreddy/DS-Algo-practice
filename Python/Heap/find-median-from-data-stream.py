'''
Idea: Median is a number which has smallest numbers on its left and largest numbers on its right.
Store the smallest numbers in a maxheap and largest numbers in a minheap
If the total nums are even the median = largest(small numbers) + smallest(large numbers) / 2
example: [1,2,3,4,5] -> [1,2,3] will be in maxheap and [4,5] in minheap
Heap insertion: O(logN)
'''
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num: int):
        if not self.maxheap or -self.maxheap[0] >= num:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        
        # If maxheap has 2 nums more than minheap then balance the two heaps by popping one from maxheap and push into minheap
        if len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
            
        elif len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self):
        # idea: Either both heaps should have equal num of elements or maxheap should have one element more
        if len(self.maxheap) == len(self.minheap):
            return ((-self.maxheap[0]) + self.minheap[0]) / 2
        else:
            return -self.maxheap[0]/1
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()