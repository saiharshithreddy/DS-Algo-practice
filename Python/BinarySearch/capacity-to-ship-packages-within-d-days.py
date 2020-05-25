# @Author: Sai Harshith
# @Date:   25-May-2020-03-05
# @Last modified by:   Sai Harshith
# @Last modified time: 25-May-2020-03-05

'''
    Very very Imp:
    Here, We have to find min ship where it takes 5 days to complete the shipments.
    So, By intuition, the minimum weight of ship should be max(weights) to accomodate that.
    The maximum weight of ship can sum of all weights to take it in 1 day.

    so, Here.. If weights=[1,2,3,4,5,6,7,8,9,10] and days=5
    If we take minimum ship weight as 10,
        [1,2,3,4],[5],[6],[7],[8],[9],[10] --> 7 days. But we only have 5 days. So increase weight.
    11->[1,2,3,4],[5,6],[7],[8],[9],[10] --> 6 days. Increase weight again.
    12 --> 13--> 14 so on. until you can divide it into 5 days.

    For this problem, this may be good. but if for some problem the ans is somewhere around 40. it takes so much time. So, Binary search comes in, where left--> max(weights) and right--> sum(weights)
    https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/256729/JavaC%2B%2BPython-Binary-Search  --> link may useful.. comments and explanation available.

    One more, in conditions below, we do not check if days==D beacuse, it may not be the minimum ship even if its same number of days. If [5,6] D=2 --> sol=6
TC: O(NlogN)
SC: O(1)

'''

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)

        while left <= right:
            mid = (left + right) // 2
            days = 1
            curr_sum = 0
            for w in weights:
                if curr_sum + w > mid:
                    curr_sum = 0
                    days += 1
                curr_sum += w
            if days > D:
                left = mid + 1
            else:
                right = mid - 1
        return left
