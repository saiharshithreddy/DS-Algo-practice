class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        # https://www.youtube.com/watch?v=RYaakWv5m6o
        
        def dfs(node, visited, prev, discovery_time):
            visited.add(node)
            low[node] = discovery_time
            
            for nei in graph[node]:
                if nei == prev:
                    continue
                    
                if nei not in visited:
                    dfs(nei, visited, node, discovery_time + 1)
                
                low[node] = min(low[node], low[nei])
                
                if low[nei] >= discovery_time + 1:
                    self.cc.append([node, nei])
                    
        visited = set()
        low = {}
        self.count = 0
        self.cc = []
        graph = collections.defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        
        dfs(0, visited, -1, 0)
        
        return self.cc
        
        # print(graph)
        
        
            
        