class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        head = self.root
        for char in word:
            if char not in head.children:

                head.children[char] = TrieNode()
            head = head.children[char]

        head.endofWord = True


    def longestWord(self, words: List[str]) -> str:


        for word in words:
            self.insert(word)


        def helper(node, partial_res):
            res = partial_res
            for char, child in node.children.items():
                if child.endofWord:
                    pot = helper(child, partial_res + char )
                    if len(pot) >len(res):
                        res = pot
                    elif len(pot) == len(res) and pot < res:
                        res = pot
            return res
        return helper(self.root, '')
        
