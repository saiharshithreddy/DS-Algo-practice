# @Author: Sai Harshith
# @Date:   2020-05-06T20:00:11-07:00
# @Last modified by:   Sai Harshith
# @Last modified time: 2020-05-22T13:00:40-07:00

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def subarraysAtmostKDistinct(A, K):

            win_start = 0
            subarray_count = 0
            num_freq = {}
            win_end = 0
            for win_end in range(len(A)):
                right_num = A[win_end]
                if right_num not in num_freq:
                    num_freq[right_num] = 1
                else:
                    num_freq[right_num] += 1

                while len(num_freq) > K:

                    left_num = A[win_start]
                    if left_num not in num_freq:
                        num_freq[left_num] = 1

                    num_freq[left_num] -= 1

                    if num_freq[left_num] == 0:
                        del num_freq[left_num]

                    win_start += 1

                subarray_count += win_end - win_start + 1
            return subarray_count

        return subarraysAtmostKDistinct(A, K) - subarraysAtmostKDistinct(A, K-1)
