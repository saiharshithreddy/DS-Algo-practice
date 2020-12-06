'''
Approach: Sort start times and end times. Use two pointers
Difficulties faced: To release a room when ended
Steps to resolve Difficulties: Sorted the times and used two pointers
Time complexity: O(NlogN)
Space complexity: O(N)
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = sorted(x[0] for x in intervals)
        end_times = sorted(x[1] for x in intervals)

        start_ptr = 0
        end_ptr = 0
        rooms = 0
        # till all meetings are ended
        while start_ptr < len(intervals):
            # check if start of a meeting is greater than end time of meeting.( means a meeting has ended so free a room)
            if start_times[start_ptr] >= end_times[end_ptr]:
                rooms -= 1
                end_ptr += 1
            # allot a room for each meeting
            rooms += 1
            start_ptr += 1
        return rooms
