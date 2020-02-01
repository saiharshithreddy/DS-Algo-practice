import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        TC: O(log(min(n,m)))
        SC: O(1)

        Partition X + Partition Y = (X + Y + 1)/2
        '''
        X, Y = len(nums1), len(nums2)
        
        # partitioning is based on smaller array
        if X > Y:
            return self.findMedianSortedArrays(nums2, nums1)
        
        low = 0
        high = X

        # binary search
        while low <= high:
            partitionX = int((low + high)/2)
            partitionY = int((X+Y+1)/2 - partitionX)
            
            '''
            we need the numbers left and right of the partition
            X: x1, x2 | x3, x4, x5
            Y: y1, y2, y3| y4, y5
            i.e x2 (max left X) x3 (min right X) and y3 (max left Y) y4 (min right Y)
            '''
            maxLeftX = -math.inf if partitionX == 0 else nums1[partitionX-1]
            minRightX = math.inf if partitionX == X else nums1[partitionX]
            
            maxLeftY = -math.inf if partitionY == 0 else nums2[partitionY-1]
            minRightY = math.inf if partitionY == Y else nums2[partitionY]
            
            # correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # if total nums are even
                if (X+Y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
                # if total nums are odd    
                else:
                    return max(maxLeftX, maxLeftY)
            # search in left side
            elif maxLeftX > minRightY:
                high = partitionX - 1
            # search in right side
            else:
                low = partitionX + 1
