from collections import defaultdict
def restoreArray(pairs):

    # visited = [False] * len(pairs)+1
    graph = defaultdict(list)
    for i in pairs:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    print(graph)


    def dfs(node, visited, curr, res):

        curr.append(node)

        if(len(curr) == len(graph)):

            res[:] = curr[:]
            return

        print(node, len(curr), len(graph))

        visited.add(node)

        for nextNode in graph[node]:
            if(nextNode not in visited):
                dfs(nextNode, visited, curr, res)

    res = []
    pos = []
    for i in list(graph):
        if(len(graph[i]) == 1):
            pos.append(i)
    print(pos)
    # for node in pos:
    visited = set()
    dfs(pos[0], visited, [], res)
    print(res)



if __name__ == '__main__':
    pairs = [[3,5],[1,4],[2,4],[1,5]]
    restoreArray(pairs)
