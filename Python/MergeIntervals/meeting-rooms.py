'''
Approach: Sort and compare end of first list with start of next list
Difficulties faced: None
Steps to resolve Difficulties: -
Time complexity: O(NlogN)
Space complexity: O(1)
'''

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])

        end = float('-inf')

        for interval in intervals:
            if interval[0] >= end:
                end = interval[-1]
            else:
                return False
        return True
