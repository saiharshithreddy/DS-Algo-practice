'''
Ebay OA question.

You had an array a of length n containing pairwise distinct integer numbers, but it's been corrupted! Fortunately, you have a list of all the pairs of numbers that were adjacent to each other in a , so you might be able to restore it.

You are given pairs , an array of n 1 elements, where pairs[i] is a 2-element array of elements from a , either in the form [a[i], a[i 1]] or [a[i 1], a[i]). Your task is to return the original array a .

NOTE: The original and reversed arrays are both considered to be correct answers. You may return either of them.

Example

For pairs = [[3, 5] [1,4], [2, 4] [1, 5]], the output can be restored Array(pairs) = [3, 5, 1, 4, 2] .

• The result of splitting the array [3, 5, 1, 4, 2] into pairs is [[3, 5], [5, 1], [1,4], [4, 2]] .

. It can be seen that this array is the same as the pairs up to permutations in some pairs and pairs shuffling.

The reversed array [2, 4, 1, s, 3] is also considered a valid answer.
'''

'''
Approach: Create a undirected graph and do DFS to get the array. Starting node/ ending node will be the node with len(adj list)=1

'''
from collections import defaultdict
def restoreArray(pairs):

    graph = defaultdict(list)
    for i in pairs:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    print('Graph', graph)

    def dfs(node, visited):
        visited.add(node)
        res.append(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei, visited)

        return

    res = []
    pos = []
    for i in list(graph):
        # only starting and ending nodes in the array have one adjacent node
        if(len(graph[i]) == 1):
            pos.append(i)

    visited = set()
    dfs(pos[0], visited)
    print('Restored array', res)



if __name__ == '__main__':
    pairs = [[1,4],[2,4],[1,5], [3,5]]
    restoreArray(pairs)
