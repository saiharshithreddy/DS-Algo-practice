'''
Idea: The numbers in the same diagonal will have same i-j 

0,1,2
3,4,5
6,7,8

1,5 are in a diagonal with i-j values -1
To have an easy lookup we can use a hashmap and store all the nums in a list 
map = { -1: [1,5]} like this 

sort each list and store back in the same matrix. 

TC: O(MNlogD) where D is the length of diagonal with D = min(M,N).
SC: O(MN)
'''
import collections
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        row = len(mat)
        col = len(mat[0])
        
        diag_ele = collections.defaultdict(list)
        
        for i in range(row):
            for j in range(col):
                diag_ele[i-j].append(mat[i][j])
                
        for pos in diag_ele:
            diag_ele[pos].sort(reverse=True)
            
        for i in range(row):
            for j in range(col):
                mat[i][j] = diag_ele[i-j].pop()
                
                
        return mat
                
        