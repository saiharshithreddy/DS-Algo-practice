# @Author: Sai Harshith
# @Date:   24-May-2020-11-05
# @Last modified by:   Sai Harshith
# @Last modified time: 24-May-2020-11-05

'''
APPROACH : GREEDY
REQUIREMENT : WE NEED LARGEST NUMBER (as right as possible) FOR THE BEGINING INDICES ## 919879 = > 999871 ( 1's largest no. is rightmost 9 )
Note the last occurance of every digit (0 to 9), as we move through the number,
if we have any digit greater than curr_digit whose index is to its right, we swap and return then and there
TC:O(N)
SC:O(N)
'''
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums_str = str(num)
        items = [int(i) for i in nums_str]

        indices = {}

        for index in range(len(items)):
            indices[items[index]] = index

        for index, n in enumerate(items):
            for i in range(9,n,-1):
                if indices.get(i,0) > index:
                    items[index], items[indices[i]] = items[indices[i]], items[index]

                    return ''.join(str(v) for v in items)
        return num
