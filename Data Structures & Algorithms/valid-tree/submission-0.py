class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
            
        # A valid tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
            
        # Step 1: Build the adjacency list
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        visit = set()
        
        def dfs(i, prev):
            if i in visit:
                return False  # Cycle detected!
                
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue  # Skip the edge we just came from
                if not dfs(j, i):
                    return False
            return True
            
        # Step 2: Start DFS from node 0 and check if all nodes are visited
        if not dfs(0, -1) or len(visit) != n:
            return False
            
        return True