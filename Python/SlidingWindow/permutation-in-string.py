# @Author: Sai Harshith
# @Date:   09-May-2020-18-05
# @Last modified by:   Sai Harshith
# @Last modified time: 11-Jun-2020-00-06



'''
Approach: Sliding window with Hashmap

Idea:
1. Store the letter, freq of the pattern in hashmap
2. Sliding window on the string and check if the letter is in hashmap. if freq = 0 then increment matched count
3. Return true when matched = len(hashmap)
4. Shrink the window when win_end > len(pattern)
5. if the letter is part of the pattern then check if its count = 0 and decrement matched. also increase the freq of that letter in hashmap
TC: O(N+k)
SC: O(k) k = len(pattern)
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        char_freq = {}
        # 1
        for i in range(len(s1)):
            if s1[i] not in char_freq:
                char_freq[s1[i]] = 1
            else:
                char_freq[s1[i]] += 1


        matched = 0
        win_start = 0
        # 2
        for win_end in range(len(s2)):
            right_char = s2[win_end]

            if right_char in char_freq:
                char_freq[right_char] -= 1
                if char_freq[right_char] == 0:
                    matched += 1
            # 3
            if matched == len(char_freq):
                return True

            # 4 shrink the window
            if win_end >= len(s1) - 1:
                left_char = s2[win_start]

                win_start += 1
                # 5
                if left_char in char_freq:
                    if char_freq[left_char] == 0:
                        matched -= 1
                    char_freq[left_char] += 1


        return False

               
