# @Author: Sai Harshith
# @Date:   12-May-2020-17-05
# @Last modified by:   Sai Harshith
# @Last modified time: 26-May-2020-12-05


'''
boyre moore voting algo
https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html

The essential concepts is you keep a counter for the majority number X.
If you find a number Y that is not X, the current counter should deduce 1.
The reason is that if there is 5 X and 4 Y, there would be one (5-4) more X than Y.
This could be explained as "4 X being paired out by 4 Y"
'''
class Solution:
    def majorityElement(self, nums: List[int]):

        candidate = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count += 1
            elif candidate != nums[i]:
                count -= 1
            else:
                count += 1
        return candidate
