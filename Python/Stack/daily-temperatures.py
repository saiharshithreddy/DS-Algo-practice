'''
Time complexity: O(T)
Space complexity: O(T)
Approach:
1. Push (day, temp) to stack
2. if curr temp > last temp in stack, pop the tuple and store the difference in days (curr_day - day) in result[day]

Observation: It's important to keep a position in the stack. Because we have to know after how many days there is increase in temp
[73, 74, 75, 71, 69, 72, 76, 73]
for 75, we see a increase in temp after 4 days (76)  how do we calc the days here? (3, 75) and (7,76) = (7-3) days
'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        stack = []
        res = [0] * len(T)

        for curr_day, curr_temperature in enumerate(T):
            while stack and curr_temperature > stack[-1][1]:
                day, temp = stack.pop()
                res[day] = curr_day - day

            stack.append((curr_day, curr_temperature))
        return res
