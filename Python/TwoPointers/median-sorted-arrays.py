'''
Approach 1: Merge both arrays and find median
TC: O(n)
SC: O(1)
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. merge two sorted arrays
        
        ptr1, ptr2 = 0,0
        p = len(nums1)+len(nums2)-1
        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] < nums2[ptr2]:
                nums1[p] = nums2[ptr2]
                ptr2 -= 1
            else:
                nums1[p] = nums1[ptr1]
                ptr1 -= 1
                
            p -=1
            
        nums1[:ptr2 + 1] = nums2[:ptr2+1]
        
        # 2. Find median
        n = len(nums1)
        # if size of the list is even
        if n%2 ==0:
            median = float(nums1[int((n/2)-1)] + nums1[int(n/2)]) / 2
        # if size is odd
        else:
            median = float(nums1[int(n/2)])
        return median

