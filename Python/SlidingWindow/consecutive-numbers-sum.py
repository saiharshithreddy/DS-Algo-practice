class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        '''# sliding window
#         nums = list(range(1,N+1))
#         start = 0
#         sum = 0
#         count = 0
#         #res = []
#         for end in range(len(nums)):
#             sum += nums[end]

#             while sum > N:
#                 sum -= nums[start]
#                 start += 1

#             if sum == N:
#                 #res.append(nums[start:end+1])
#                 count += 1
#         #print(N, res)
#         return count
'''
        # Not my solution
        # sliding window approach did not run in the time specified for the program in leetcode. but logic was correct.
        # if asked in an video interview. Sliding window approach will suffice.
        while N & 1 == 0:
            N >>= 1

        ans = 1
        d = 3
        while d * d <= N:
            e = 0
            while N % d == 0:
                N /= d
                e += 1
            ans *= e + 1
            d += 2

        if N > 1: ans *= 2
        return ans
