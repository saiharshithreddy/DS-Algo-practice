# @Author: Sai Harshith
# @Date:   08-May-2020-01-05
# @Last modified by:   Sai Harshith
# @Last modified time: 26-May-2020-13-05



'''

Approach: Hashmap to store the sums

Time complexity: O(N)
Space complexity: O(N)

Algorithm:
1. Initialize the hashmap with 0: 1
2. Check if sum-k exists in hashmap
3. Add sum to the hashmap
    Inc counter if sum exists in hashmap
'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_count = {}
        sum_count[0] = 1
        count = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]

            # main condition
            if sum-k in sum_count:
                count += sum_count[sum-k]


            if sum not in sum_count:
                sum_count[sum] = 1
            else:
                sum_count[sum] += 1

        return count
