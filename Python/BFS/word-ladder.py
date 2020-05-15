import collections

'''
BFS to find the shortest path
TC: O(M^2 * N)
SC: O(M^2 * N) 
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        
        from collections import defaultdict
        
        
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        
        lookup = defaultdict(list)
        # O(N)
        for word in wordList:
            # O(M)
            for i in range(len(beginWord)):
                
                lookup[word[:i] + "*" + word[i+1:]].append(word)
                '''
                defaultdict(<class 'list'>, {'*ot': ['hot', 'dot', 'lot'], 'h*t': ['hot'], 'ho*': ['hot'], 'd*t': ['dot'], 'do*': ['dot', 'dog'], '*og': ['dog', 'log', 'cog'], 'd*g': ['dog'], 'l*t': ['lot'], 'lo*': ['lot', 'log'], 'l*g': ['log'], 'c*g': ['cog'], 'co*': ['cog']})

                '''
        
        queue = collections.deque()
        queue.appendleft((beginWord, 1))
        # print(queue)
        visited = {beginWord : True}
        # O(N)
        while queue:
            curr_word, path_len = queue.popleft()
            # O(M)
            for i in range(len(beginWord)):
                pattern = curr_word[:i] + "*" + curr_word[i+1:]
                #O(M)
                for word in lookup[pattern]:
                    if curr_word == word:
                        continue
                    if word == endWord:
                        return path_len + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, path_len + 1))
                     
        return 0 