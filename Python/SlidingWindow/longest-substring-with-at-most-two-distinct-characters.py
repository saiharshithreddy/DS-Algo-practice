class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_map = {}
        win_start = 0
        max_length = 0

        for win_end in range(len(s)):
            right_char = s[win_end]
            if right_char not in char_map:
                char_map[right_char] = 0
            char_map[right_char] += 1

            while len(char_map) > 2:
                left_char = s[win_start]
                char_map[left_char] -= 1
                if char_map[left_char] == 0:
                    del char_map[left_char]
                win_start += 1
            max_length = max(max_length, win_end - win_start + 1)
        return max_length
