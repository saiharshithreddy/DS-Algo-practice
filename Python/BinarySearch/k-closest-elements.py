'''
Approach: Binary Search + Two pointers
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(logN + k)
Space complexity: O(1)
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #base case
        if len(arr)<=1:
            return arr
        # returns the index of the num closest/equal to x
        index = self.binarysearch(arr,x, 0, len(arr)-1)
        # two pointers
        left = index
        right = index + 1
        result = []
        size = len(arr)
        # to find k closest nums O(K)
        for i in range(k):
            if left >= 0 and right <size:
                # check for the difference
                diff_1 = abs(x - arr[left])
                diff_2 = abs(x - arr[right])
                # add the smallest difference
                if diff_1 <= diff_2:
                    # to the first of the list as the result array has to be sorted
                    result.insert(0,arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1
            # if the index found is at the last of the list.
            elif left > 0:
                result.insert(0,arr[left])
                left -= 1
            # if the index found is at the first of the list
            elif right < size:
                result.append(arr[right])
                right += 1
        return result


    def binarysearch(self, arr,x, low, high):
        # O(logN)
        while low<= high:
            mid = low+(high-low)//2
            if arr[mid]==x:
                return mid

            elif arr[mid]<x:
                low = mid+1

            else:
                high = mid-1
        return mid
