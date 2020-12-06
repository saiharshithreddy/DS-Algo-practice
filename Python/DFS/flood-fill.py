'''
Approach: DFS, Similar to Number of islands - instead of calling dfs on multiple 1s by looping through the matrix
DFS() is perfomed on one cell image[sr][sc] 
Time complexity : O(MN) where M is the number of rows and N is the number of columns.
Space complexity : worst case O(M N) in case that the grid map is filled with lands where DFS goes by M×N deep
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int):
        # base case when the new color is same as the old color.
        if image[sr][sc] == newColor:
            return image

        def dfs(image, i,j):
            # out of bounds and when the cell has a different color - func return
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
        # get the color of the starting cell and check the color of its adjacent cells and update their color to the new color
        color = image[sr][sc]

        dfs(image, sr, sc)

        return image
