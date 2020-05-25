'''
Approach 1: Max heap 
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return
        if len(nums) == k:
            heap = nums
            heapq._heapify_max(heap)
            return [heap[0]]

        win_start, win_end = 0, k - 1
        res = []

        heap = nums[win_start:win_end + 1]
        heapq._heapify_max(heap)

        # get the max val
        res.append(heap[0])

        first_in_window = nums[win_start]
        win_start += 1
        win_end += 1
        next_num = nums[win_end]
        n = len(nums)
        # For every remaining element
        while win_end < n:

            # Add the next element of the window to the heap
            heap[heap.index(first_in_window)] = next_num

            # Heapify to get the maximum
            heapq._heapify_max(heap)
            # get the max
            res.append(heap[0])
            first_in_window = nums[win_start]
            win_start += 1
            win_end += 1
            if win_end < n:
                next_num = nums[win_end]
        return res
