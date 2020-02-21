
'''
Approach: Sliding window and dictionary
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(N)
Space complexity: O(N)
'''
class Solution:
    def totalFruit(tree) :
        window_start = 0
        max_window_len = 0
        hash_map = {}

        for window_end in range(len(tree)):
        # store the values in the dictionary
            if tree[window_end] not in hash_map:
                hash_map[tree[window_end]] = 1
            else:
                hash_map[tree[window_end]] += 1
            # When more than 2 types of fruits
            while len(hash_map) > 2:
                # Get the number of fruits of fruit type 1
                left_fruit = tree[window_start]
                # decrement the num
                hash_map[left_fruit] -= 1
                # if num of fruits is 0
                if hash_map[left_fruit] == 0:
                    del hash_map[left_fruit]
                # move the window to the right
                window_start += 1
            # find the max window size
            max_window_len = max(max_window_len, window_end - window_start + 1)
        return max_window_len
