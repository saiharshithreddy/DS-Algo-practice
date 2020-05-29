# @Author: Sai Harshith
# @Date:   25-May-2020-15-05
# @Last modified by:   Sai Harshith
# @Last modified time: 25-May-2020-15-05
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = collections.Counter(
            word for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans
