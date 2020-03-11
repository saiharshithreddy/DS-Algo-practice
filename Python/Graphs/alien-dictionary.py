class Solution:
    def alienOrder(self, words: List[str]) -> str:
        self.graph = collections.defaultdict(list)

        for i in range(1,len(words)):
            pt = 0
            while pt < len(words):

                if words[i-1][pt] != words[i][pt]:
                    self.graph[words[i-1][pt]].append(words[i][pt])
                    break
                pt += 1

        print(self.graph)

        def hasCycle(node):
            visited = set()
