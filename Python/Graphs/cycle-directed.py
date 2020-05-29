# @Author: Sai Harshith
# @Date:   14-Feb-2020-19-02
# @Last modified by:   Sai Harshith
# @Last modified time: 27-May-2020-11-05

def hasCycle(node, exploring, explored):

    if node in exploring:
        return True
    if node in explored:
        return False

    exploring.add(node)
    # Its neighbors
    for nei in self.graph[node]:
        if hasCycle(nei, exploring, explored):
            return True

    explored.add(node)
    exploring.remove(node)
    return False
