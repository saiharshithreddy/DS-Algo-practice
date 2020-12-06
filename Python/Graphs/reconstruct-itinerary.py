'''
Approach: 

Time complexity: O(E/2 * log E/2)
Space complexity: O(V + 2E)

Algorithm:
1. Sort the neighbors of the graph in reverse order
2. Pop the neighbor and do DFS
3. Add the node to the result when its neighbor list is empty
4. Reverse the result list
'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        for origin, itinerary in self.flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort(reverse=True)


        self.result = []
        self.DFS('JFK')

        return self.result[::-1]

    def DFS(self, origin):
        destlist = self.flightMap[origin]
        while destlist:
            nextDest = destlist.pop()
            self.DFS(nextDest)

        self.result.append(origin)

