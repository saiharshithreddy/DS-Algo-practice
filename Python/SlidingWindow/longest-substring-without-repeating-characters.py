'''
Time complexity: O(N)
Space complexity: O(k), k is number of unique characters
Algorithm:
1. Use a dictionary to store the position of the characters
2. If the dictionary contains a character shrink the window to +1 position from that character.
3. Find the max of max_length and window_length
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # sliding window strategy
        
        # use dictionary to store the position of the characters appearing in the string
        window_start = 0
        max_length = 0
        dictionary = {}

        for window_end in range(len(s)):
            right_char = s[window_end]
            # sliding window shrinking condition
            if right_char in dictionary:
                window_start = max(window_start, dictionary[right_char]+1)
            
            
            # if element not in dictionary
            dictionary[right_char] = window_end
            max_length = max(max_length, window_end - window_start + 1)
            
            
        return max_length
        
        