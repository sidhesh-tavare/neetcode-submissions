"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not Node : return None 
        mapper = {} #maps old to nwe
        def dfs(node):
            if node is None : return None
            if node in mapper : return mapper[node]
            clone =Node(node.val)
            mapper[node] = clone

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return mapper[node]

        return dfs(node)

        