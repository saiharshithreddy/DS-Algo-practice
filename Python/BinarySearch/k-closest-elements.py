# @Author: Sai Harshith
# @Date:   08-Feb-2020-19-02
# @Last modified by:   Sai Harshith
# @Last modified time: 24-May-2020-15-05



'''
Approach 1:
Binary search to find the index of a number closest to X
TC: logN for binary search + KlogK for heap + KlogK for sort
SC: O(K) for heap
'''

class Solution:
    def findClosestElements(self, arr: List[int], K: int, X: int) -> List[int]:
        index = self.binary_search(arr, X)
        low, high = index - K, index + K

        # to avoid out of bounds of the array
        low = max(low, 0)  # 'low' should not be less than zero
        # 'high' should not be greater the size of the array
        high = min(high, len(arr) - 1)


        minHeap = []
        # add all candidate elements to the min heap, sorted by their absolute difference from 'X'
        for i in range(low, high + 1):
            heappush(minHeap, (abs(arr[i] - X), arr[i]))

        # we need the top 'K' elements having smallest difference from 'X'
        result = []
        for _ in range(K):
            result.append(heappop(minHeap)[1])

        # sort because the closest numbers must be in ascending order as per the ques
        result.sort()
        return result

    '''
    In standard Binary search we return -1 if the number is not present in the array. But in this we need to find
    the closest index to the number we want to search. So we return mid.
    '''
    def binary_search(self, arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return mid

# =========================================================================
'''
Approach 2:
Binary search to find the index
Two pointers to find k closest to the index num
TC: O(logN) for binary search + O(k)
SC: O(k) for result array
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr)<=1:
            return arr
        index = self.binarysearch(arr,x, 0, len(arr)-1)
        # two pointers
        left = index
        right = index + 1

        result = collections.deque()
        size = len(arr)

        for i in range(k):
            # left and right are in valid range of arr
            if left >= 0 and right <size:
                # find the difference of x and left and x and right
                diff_1 = abs(x - arr[left])
                diff_2 = abs(x - arr[right])
                # if difference with left is small then add it to front because the result should be sorted.
                if diff_1 <= diff_2:
                    result.appendleft(0,arr[left])
                    left -= 1

                else:
                    result.append(arr[right])
                    right += 1
            # if right is out of bounds ( last element is the closest to X)
            elif left > 0:
                result.appendleft(0,arr[left])
                left -= 1
            # if left is out of bounds
            elif right < size:
                result.append(arr[right])
                right += 1

        return result


    def binarysearch(self, arr,x, low, high):

        while low<= high:

            mid = low+(high-low)//2

            if arr[mid]==x:
                return mid

            elif arr[mid]<x:
                low = mid+1

            else:
                high = mid-1

        return mid
