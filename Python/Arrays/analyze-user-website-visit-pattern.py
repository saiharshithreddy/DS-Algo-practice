# @Author: Sai Harshith
# @Date:   22-May-2020-17-05
# @Last modified by:   Sai Harshith
# @Last modified time: 22-May-2020-17-05

'''

'''

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        dp = collections.defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            dp[u].append(w)


        counter_dict = defaultdict(int)
        for website_list in dp.values():
            combs = set(combinations(website_list, 3))

            for comb in combs:
                counter_dict[comb] += 1


        sequence = sorted(counter_dict, key=lambda x: (-counter_dict[x], x))
        return sequence[0]
