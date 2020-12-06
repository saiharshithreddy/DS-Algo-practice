'''
Approach:
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O()
Space complexity: O()
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        # base case
        if s == "":
            return s
        char_freq = {}
        # store the frequency
        for c in range(len(s)):
            if s[c] not in char_freq:
                char_freq[s[c]] = 1
            else:
                char_freq[s[c]] += 1

        # sort based on frequency
        li = sorted(char_freq.items(), key =
             lambda kv:( kv[1],kv[0]), reverse=True)

        result = ""

        for x in li:
            result += x[0]*x[1]

        return result
