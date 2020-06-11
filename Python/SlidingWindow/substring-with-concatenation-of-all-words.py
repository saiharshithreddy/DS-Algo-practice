# @Author: Sai Harshith
# @Date:   09-May-2020-20-05
# @Last modified by:   Sai Harshith
# @Last modified time: 11-Jun-2020-00-06


'''
Approach:

Time complexity: O(N)
Space complexity: O(N) for hashmap

Algorithm:

'''
class Solution:
    def findSubstring(self, s, words):

        word_map = {}
        # hashmap for words
        for word in words:
            if word not in word_map:
                word_map[word] = 1
            else:
                word_map[word] += 1
