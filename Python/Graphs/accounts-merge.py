# @Author: Sai Harshith
# @Date:   22-May-2020-18-05
# @Last modified by:   Sai Harshith
# @Last modified time: 22-May-2020-18-05

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:


        def dfs(node, visited):
            visited.add(node)
            mails.append(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, visited)
        mails = []
        user_mail = defaultdict()
        visited = set()
        res = []

        graph = collections.defaultdict(set)

        for acc in accounts:
            user_mail[acc[1]] = acc[0]
            for mail in acc[1:]:
                graph[acc[1]].add(mail)
                graph[mail].add(acc[1])


        # call dfs
        for mail in list(graph):
            if mail not in visited: # to call only if the node is unvisited
                dfs(mail, visited)
                name = user_mail[mail]

                res.append([name] + sorted(mails))
                mails = []
        return res

        
