'''
Approach: DFS 

Time complexity: O(2^N)
Space complexity: O(2^N)

Algorithm:
1. Add ( until = n
2. Add ) only when count of ) is less than (
'''
class Solution:
    def generateParenthesis(self, n):
        def helper(braces,open_para,closed_para):
            
            if(len(braces)==2*n):
                self.result.append(braces)
                return

            if(open_para<=n):
                helper(braces+"(",open_para+1,closed_para)

            if(closed_para<open_para):
                helper(braces+")",open_para,closed_para+1)


        self.result=[]
        helper("",1,1)
        return self.result

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))