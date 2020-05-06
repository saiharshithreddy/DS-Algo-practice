# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # version num starts from 1
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                # once a bad version is found we have to check if there is a bad version earlier.
                # to get the first version right is moved to mid
                right = mid
            else:
                left = mid + 1
        return left
