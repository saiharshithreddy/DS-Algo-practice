'''
Approach:
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O()
Space complexity: O()
'''

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        result =[]

        i,j=0,0
        while i< len(A) and j< len(B):

            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])

            if low <= high:
                result.append([low, high])

            #
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1


        return result
