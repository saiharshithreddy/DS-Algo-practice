# @Author: Sai Harshith
# @Date:   25-May-2020-11-05
# @Last modified by:   Sai Harshith
# @Last modified time: 25-May-2020-11-05
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashset = set()
        for ch in s:
            if ch not in hashset:
                hashset.add(ch)
            else:
                hashset.remove(ch)
        # len(hash) is the number of the odd letters. hashset contains only odd characters.
        # a palindrome can be of odd length with a character with odd freq and letters to its left and right with even freq. ex: aaaabcccc that is len(s) - len(odd letters) +1 so that we can include one odd freq letter.
        return len(s) - len(hashset) + 1 if len(hashset) > 0 else len(s)
        
