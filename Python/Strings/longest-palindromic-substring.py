# @Author: Sai Harshith
# @Date:   22-May-2020-13-05
# @Last modified by:   Sai Harshith
# @Last modified time: 22-May-2020-13-05

'''
Expand around the center
aba is a palindrome and aa is a palindrome
TC: O(N^2)
SC: O(1)
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr_longest = [0,1]
        for i in range(1,len(s)):
            odd = self.getlongestPalindrome(s,i-1,i+1)
            even = self.getlongestPalindrome(s,i-1,i)
            longest_pal = max(odd,even,key=lambda x: x[1] - x[0])
            curr_longest = max(longest_pal, curr_longest, key=lambda x:x[1] - x[0])
        return s[curr_longest[0] : curr_longest[1]]

    def getlongestPalindrome(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        return [left+1, right]
