class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()

        left, right = 0, len(A)-1
        closest_sum = -1

        while left < right:
            curr_sum = A[left] + A[right]
            if curr_sum < K:
                closest_sum = max(closest_sum, curr_sum)
                left += 1
            else:
                right -= 1

        return closest_sum

        
