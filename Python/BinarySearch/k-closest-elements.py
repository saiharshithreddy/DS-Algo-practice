'''
Approach: Binary Search + Two pointers
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(logN + k)
Space complexity: O(1)
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr)<=1:
            return arr
        index = self.binarysearch(arr,x, 0, len(arr)-1)
        left = index
        right = index + 1
        result = []
        size = len(arr)
        for i in range(k):
            if left >= 0 and right <size:
                diff_1 = abs(x - arr[left])
                diff_2 = abs(x - arr[right])
                if diff_1 <= diff_2:
                    result.insert(0,arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1
            elif left > 0:
                result.insert(0,arr[left])
                left -= 1
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
