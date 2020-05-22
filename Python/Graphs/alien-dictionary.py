'''
Approach: Topological sort + Cycle detection

Chillar edge case: word 1 in the word list is bigger than next word and has word2 as it prefix. 

'''
class Solution:
    def alienOrder(self, words: List[str]):
        def hasCycle(node, exploring, explored):
            if node in exploring:
                return True
            if node in explored:
                return False
            exploring.add(node)
            
            for nei in graph[node]:
                if hasCycle(nei, exploring, explored):
                    return True
            result.appendleft(node)
            explored.add(node)
            exploring.remove(node)
            return False
        
        # create graph
        graph=collections.defaultdict(list)

        x,y=0,1
        while(y<len(words)):
            i=j=0
            word1,word2=words[x],words[y]
            
            # condition for chillar test case 
            if word1.startswith(word2) and len(word1) > len(word2):
                return ""
            
            while(i<len(word1) and j<len(word2)):
                if(word1[i]==word2[j]):
                    i+=1
                    j+=1
                else:
                    graph[word1[i]].append(word2[j])
                    break
            x+=1
            y+=1
        # create nodes in the graph with empty adjacency list
        all_chars=set("".join(words))
        missed_chars = all_chars - set(graph)
        
        for char in missed_chars:
            graph[char]=[]
        
        
        exploring = set()
        explored = set()
        result = collections.deque()
        for node in list(graph):
            if hasCycle(node, exploring, explored):
                return ""
        
        return "".join(result)