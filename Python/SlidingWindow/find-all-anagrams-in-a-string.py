# @Author: Sai Harshith
# @Date:   09-May-2020-19-05
# @Last modified by:   Sai Harshith
# @Last modified time: 27-May-2020-11-05



'''
Same as #567 Permutations in string
Only change is here we are storing the starting indices of the anagrams

Approach: Sliding window with Hashmap

Idea:
1. Store the letter, freq of the pattern in hashmap
2. Sliding window on the string and check if the letter is in hashmap. if freq = 0 then increment matched count
3. Store the starting index of the anagram when matched = len(hashmap)
4. Shrink the window when win_end > len(pattern)
5. if the letter is part of the pattern then check if its count = 0 and decrement matched. also increase the freq of that letter in hashmap
TC: O(N+k)
SC: O(k) k = len(pattern)
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        char_freq = {}
        indices = []
        matched = 0
        win_start = 0
        # 1
        for char in p:
            if char not in char_freq:
                char_freq[char] = 1
            else:
                char_freq[char] += 1


        # 2
        for win_end in range(len(s)):
            right_char = s[win_end]

            if right_char in char_freq:
                char_freq[right_char] -= 1
                if char_freq[right_char] == 0:
                    matched += 1
            # 3
            if matched == len(char_freq):
                indices.append(win_start)

            # 4 shrink the window
            if win_end >= len(p) - 1:
                left_char = s[win_start]

                win_start += 1
                # 5
                if left_char in char_freq:
                    if char_freq[left_char] == 0:
                        matched -= 1
                    char_freq[left_char] += 1


        return indices
