'''
Did it run on leetcode:
Did you face any problem:
Time Compelxity:
Space Complexity:
Algorithm:

'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)-1):
            #for j in sublist:
            sublist = intervals[i]
            nextlist = intervals[i+1]
            nextlist[0] <= sublist[len(sublist)-1]
            merged = 
