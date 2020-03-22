'''
Approach: DFS 

Time complexity: O(2^N)
Space complexity: O(2^N)

Algorithm:
1. Add ( until = n
2. Add ) only when count of ) is less than (
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(braces,o,c):
            if(len(braces)==2*n):
                self.result.append(braces)
                return

            if(o<=n):
                helper(braces+"(",o+1,c);
            if(c<o):
                helper(braces+")",o,c+1)


        self.result=[]
        helper("",1,1)
        return self.result
