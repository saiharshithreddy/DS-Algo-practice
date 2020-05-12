class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1
            
        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1
        # print(left, right)
        
        queue = collections.deque()
        word = ""
        while left<= right:
            # if we reach ' ' then left word is finished
            if s[left] == ' ' and word:
                queue.appendleft(word)
                word = ""
            # character of the left word is added 
            elif s[left] != ' ':
                word += s[left]
            left += 1
        queue.appendleft((word))
        
        return ' '.join(queue)