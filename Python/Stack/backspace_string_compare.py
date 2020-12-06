'''
Approach 1: Two pointers
Version 1: Did not handle the case of having consecutive #s. Did not run on leetcode
TC: 
SC:
'''


'''
Approach 2: Stack
TC: O(n+m)
SC: O(1)
'''

class Solution:
   
    def backspaceCompare(self, S: str, T: str) -> bool:
        # use stack
        def stack(S):
            result = []
            for char in S:
                if char != '#':
                    # push
                    result.append(char)
                elif result:
                    
                    result.pop()
            return ''.join(result)
        
        return stack(S) == stack(T)

