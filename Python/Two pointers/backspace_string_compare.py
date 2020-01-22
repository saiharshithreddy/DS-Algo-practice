
class Solution:
    '''
    Approach 1: Two pointers
    Version 1: Did not handle the case of having consecutive #s. Did not run on leetcode
    TC: 
    SC:
    '''
    def backspaceCompare(self, S: str, T: str) -> bool:
        ptr1, ptr2 = len(S),len(T)
        
        compare_bool = True
        while ptr1 > 0 and ptr2 > 0:
            if S[ptr1-1] == T[ptr2-1] and S[ptr1-1] == '#':
                
                ptr1 -= 1
                ptr2 -= 1            

            elif S[ptr1-1] == T[ptr2-1] and S[ptr1-1] == '#':
                ptr1 = ptr1 - 2
                ptr2 = ptr2 - 2
                
            else:
                compare_bool = False
                break
        return compare_bool