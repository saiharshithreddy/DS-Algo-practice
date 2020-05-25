# @Author: Sai Harshith
# @Date:   25-May-2020-11-05
# @Last modified by:   Sai Harshith
# @Last modified time: 25-May-2020-12-05

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        result =[]
        # sorting based on start times is must
        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])
        i,j=0,0

        while i< len(slots1) and j< len(slots2):
            # get the start_time feasible for both employees
            start_time = max(slots1[i][0], slots2[j][0])
            # min of end times
            end_time = min(slots1[i][1], slots2[j][1])

            # if start time of on employee + meeting duration is less than or equal to end time then possible meeting.
            if start_time + duration <= end_time:
                return [start_time, start_time + duration]

            # increment based on end times. 
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1


        return []
