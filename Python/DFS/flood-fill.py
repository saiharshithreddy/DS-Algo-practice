class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int):
        if image[sr][sc] == newColor:
            return image
        
        def dfs(image, i,j):
            
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != color:
                return
            
            # update the color
            image[i][j] = newColor
            # move in 4 directions
            for x,y in move(i,j):
                dfs(image, x, y)

          
        def move(i,j):
            directions  = [[0,1],[1,0],[-1,0],[0,-1]]
            for x,y in directions:
                if 0 <= i + x < row or 0 <= j + y < col:
                    yield i + x, j + y
        
        row = len(image)
        col = len(image[0])
        color = image[sr][sc] 

        dfs(image, sr, sc)
        
        return image



        