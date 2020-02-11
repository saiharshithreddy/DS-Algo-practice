'''
Approach: Min num of intervals to remove, so end should be minimum
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(NlogN)
Space complexity: O(1)

Notes: If [1,100] [1,11] [11,22] are the intervals.
1) Initialize start = 1 end = 100
2) as 1,11 overlaps with 1,100 you would want to remove it. but 11,22 will also overlap with 1,100. We have to find min intervals to remove.
so update the end with min of two overlapping intervals.
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if len(intervals)==0:
            return 0
        # O(NlogN)
        intervals.sort(key=lambda x: x[0])

        end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            # overlapping condition
            if intervals[i][0] < end:
                # main logic
                end = min(intervals[i][1], end)
                count += 1
            else:
                # update end
                end = intervals[i][1]

        return count
