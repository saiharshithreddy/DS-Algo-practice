'''
TC: O(N)
SC: O(1)
1. Reverse the array
2. Reverse 1st k elements
3. Reverse k+1 to end elements
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(arr, start, end):
            # two pointer swap
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(nums)
        # k can be greater than n
        k = k % n

        reverse(nums,0, n-1)
        reverse(nums, 0,k-1)
        reverse(nums, k, n-1)
