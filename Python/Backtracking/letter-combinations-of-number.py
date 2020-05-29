# @Author: Sai Harshith
# @Date:   12-Apr-2020-19-04
# @Last modified by:   Sai Harshith
# @Last modified time: 27-May-2020-11-05



class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_toLetter = {'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                result.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in num_toLetter[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
        result = []
        if digits:
            backtrack("", digits)
        return result
