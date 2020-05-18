class Solution:
    def sortedSquares(self, A: List[int]):
        left, right = 0, len(A)-1
        output = []
        
        while left <= right:
            if A[left]**2 >= A[right]**2:
                output.insert(0,A[left]**2) # inserts in the front of the list (largest num is chosen first and inserted in n-1 th
                                            # position)
                left += 1
               
            else:
                output.insert(0, A[right]**2)
                right -= 1
                
        return output
                
        
        