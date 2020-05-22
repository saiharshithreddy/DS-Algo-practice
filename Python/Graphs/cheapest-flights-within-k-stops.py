
'''
Dijkstra's algorithm
Similar to #1135. Connecting Cities With Minimum Cost

Directed graph 

Algorithm: Priority Queue to get the path with minimum cost. 
TC: O(V + ElogV) ; ElogV for minheap
SC: O(V+E)
'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int):
    
        graph = collections.defaultdict(dict)
        
        for city1, city2, cost in flights:
            graph[city1][city2] = cost
            
        print(graph)
        minheap = [(0, src, K)]
        
        while minheap:
            cost, city1, k = heapq.heappop(minheap)
            
            if city1 == dst:
                return cost

            # if the cities are in at most k stops away add them to the heap. 
            # for city 0 there are two neighboring cities so we need to travel to a city with and we have to choose min cost to reach the destination city.

            if k >= 0:
                for nei_city in graph[city1]:
                    nei_cost = graph[city1][nei_city]
                    heapq.heappush(minheap, (cost + nei_cost, nei_city, k-1))
            
            
        return -1
            
        