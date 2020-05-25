# @Author: Sai Harshith
# @Date:   24-May-2020-19-05
# @Last modified by:   Sai Harshith
# @Last modified time: 24-May-2020-19-05
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:

        graph = collections.defaultdict(list)

        for city1, city2, cost in connections:
            graph[city1].append((cost,city2))
            graph[city2].append((cost,city1))

        queue = [(0,N)]
        visited = set()
        total_cost = 0
        path = {}
        while queue and len(visited) != N:
            cost, city = heapq.heappop(queue)
            # if (cost,city) not in path:
            #     path[(cost,city)] = N
            if city not in visited:
                visited.add(city)
                total_cost += cost

                for cost, city in graph[city]:
                    heapq.heappush(queue, (cost,city))
        return total_cost if len(visited) == N else -1
