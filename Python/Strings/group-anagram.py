import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
       #   1. depending on the alphabet count we figure anagram and store them in a hashmap.
        
        lookup = collections.defaultdict(list)
        for word in strs:
            alphabetCount = [0] * 26
            for alphabet in word:
                alphabetCount[ord(alphabet.lower()) - 97] += 1
            
            pattern = tuple(alphabetCount)                          # hashmap can have tuples on the left side.
            lookup[pattern].append(word)
            
        return lookup.values()                
