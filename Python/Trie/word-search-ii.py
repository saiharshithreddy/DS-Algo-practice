# @Author: Sai Harshith
# @Date:   04-May-2020-20-05
# @Last modified by:   Sai Harshith
# @Last modified time: 24-May-2020-21-05
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        
        def insert(word):
            node=self.root
            for letter in word:
                if letter not in node.children:
                    node.children[letter]=TrieNode()
                node=node.children[letter]
            node.endofword=True
            
        def search(node, i, j, path):
            visited.add((i,j))
            if path in words and node.endofword == True:
                self.res.add(path)
                
            # traversing in 4 directions
            for x,y in [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]:
                if 0<= x < len(board) and 0<= y < len(board[0]) and (x,y) not in visited and board[x][y] in node.children:
                        
                    search(node.children[board[x][y]], x,y, path + board[x][y])
            
            # backtrack
            visited.remove((i,j))
            
            
        # building a trie with all words    
        
        for word in words:
            insert(word)
        visited = set()
        self.res = set()
        node = self.root 
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] in node.children:
                    search(node.children[board[i][j]], i, j,  board[i][j])
                
        return self.res
            
        