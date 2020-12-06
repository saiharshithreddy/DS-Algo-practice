class Solution:
    def reverseVowels(self, s: str) -> str:
        
        # create a dictionary
        # a e i o u
        vowels = {'a':1,'e':1,'i':1,'o':1,'u':1}
        
        left, right = 0, len(s)-1
        
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            elif s[left] in vowels and s[right] in vowels:
                # swap
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1
        return s
                
                
        
        