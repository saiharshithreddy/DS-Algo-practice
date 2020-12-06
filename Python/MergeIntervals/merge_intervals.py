'''
Approach: Keep updating start and end until there is a merged list
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(NlogN) sorting
Space complexity: O(N) for result list
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(NlogN)
        intervals.sort(key=lambda x: x[0])

        result = []
        if len(intervals) == 0:
            return result
        # initialize
        start = intervals[0][0]
        end = intervals[0][1]
        # check for start of next list < end of last list
        for i in range(1,len(intervals)):

            if intervals[i][0] <= end:
                end = max(intervals[i][1], end)

            else:
                result.append([start, end])
                # update
                start = intervals[i][0]
                end = intervals[i][1]
        # add last interval
        result.append([start,end])

        return result
