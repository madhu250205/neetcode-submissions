class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            # Base case: if node is None, return None
            if not node:
                return None
            
            # If we've already cloned this node, return the existing clone from our hash map
            if node in oldToNew:
                return oldToNew[node]
            
            # Create the clone for the current node
            copy = Node(node.val)
            oldToNew[node] = copy
            
            # Recursively clone all neighbors and append them to the copy's neighbor list
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy

        return dfs(node)