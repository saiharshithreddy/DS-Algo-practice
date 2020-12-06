'''
Approach: Sort the words list. Using trie to store 3 words starting with a letter. If there are more than 3 words then next letter will store the words.
M
|
[mobile, moneypot, monitor]
'''
class TrieNode:
    def __init__(self):
        self.children={}
        self.suggestions=[]

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root=TrieNode() # always root will be empty trienode
        products.sort() #O(NlogN)
        for prod in products:
            node=root
            for letter in prod:
                if(letter not in node.children):
                    node.children[letter]=TrieNode()
                node=node.children[letter]
                if(len(node.suggestions)<3):
                    node.suggestions.append(prod)
        result=[]
        for letter in searchWord:
            if(root):
                root=root.children.get(letter,None)
            result.append(root.suggestions if root else [])

        return result
