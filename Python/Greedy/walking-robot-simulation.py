'''
Firstly, robot doesn't face north as stated in the explanation. When i consider north, i imagine robot faces upwards but its initial direction is to right actually.
Note: This is a similar question to Robot Room cleaner (No: 489).
Code explanation:
At first, we should make obstacles as set for O(1) check for obstacles and we simply move according to command if there is no obstacle.
Critical part is the directions array in my opinion. It is a simplified move to next i and j in array form for "right", "up", "left", "down" respectively.
We also change d variable, which is direction variable as move index, when we get -2 or -1 command.
If command is -2, we should turn left, which is to increment direction index.
If command is -1, we should turn right, which is to decrement direction index.
Else, we can walk through untill face an obstacle or not.
And we update mx value in each move also.
'''

class Solution:
    def robotSim(self, commands, obstacles):