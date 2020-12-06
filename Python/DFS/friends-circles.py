'''
APPROACH : DFS 
1. Each row is a person i.e 3x3 matrix has 3 persons friend’s details.
2. Each column in a row represents its friendship with that person
3. say person0 => row_index = 0 => [1,1,0] => [friend with himself, friend with person1, not friend with person2]
4. go to each person and dfs all his friends but make sure to not re-visit.
https://www.youtube.com/watch?v=TKHIC6muurM

TC: O(N^2)
SC: O(N)
'''
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        count=0
        seen=set()
        for person_num in range(len(M)):
            if(person_num not in seen):
                count+=1
                self.friendDFS(person_num,M,seen)
        
        return count
    
    def friendDFS(self,person_num,M,seen):
        
        for index,is_friend in enumerate(M[person_num]):
            if(is_friend==1 and index not in seen):
                seen.add(index)
                self.friendDFS(index,M,seen)