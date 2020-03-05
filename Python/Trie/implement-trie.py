
'''
Algorithm:
1. Create a trienode class
2. Insert: Add the first char to the node and its children in a dictionary
3. If endofword is True then the entire string is found in the trie.
'''
class TrieNode:
    def __init__(self):
        # self.char = char
        self.children = {}
        self.endofword = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    # O(l) l: length of the string
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        head = self.root
        for char in word:
            if char not in head.children:
                node = TrieNode()
                head.children[char] = node

            head = head.children[char]
        head.endofword = True
    # O(l)
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.endofword




    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
