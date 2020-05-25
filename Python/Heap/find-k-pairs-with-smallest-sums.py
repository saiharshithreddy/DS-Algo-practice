# @Author: Sai Harshith
# @Date:   24-May-2020-15-05
# @Last modified by:   Sai Harshith
# @Last modified time: 24-May-2020-15-05

'''
Generating all the pairs and checking if their sum is smallest is not the optimum way
Why because we are not utilising the condition that the arrays are sorted so first element from array 1
and first element from array 2 will give you a small sum. So we can generate only k*k pairs instead of m*n pairs.

TC: O(NMlogK)
Sc: O(k)
'''
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        max_heap = []
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                pair_sum = nums1[i] + nums2[j]
                if len(max_heap) < k:
                    heapq.heappush(max_heap, (-pair_sum, i,j))
                else:
                    # if the new sum is greater then we can break because we need smallest.
                    if pair_sum > -max_heap[0][0]:
                        break
                    else:
                        heapq.heappushpop(max_heap, (-pair_sum, i, j))

        res = []
        for pair_sum, i, j in max_heap:
            res.append([nums1[i], nums2[j]])

        return res
