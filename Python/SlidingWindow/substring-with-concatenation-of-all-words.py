class Solution:
    def findSubstring(self, s, words):
            
        word_map = {}
        # hashmap for words 
        for word in words:
            if word not in word_map:
                word_map[word] = 1
            else:
                word_map[word] += 1
        
        
        