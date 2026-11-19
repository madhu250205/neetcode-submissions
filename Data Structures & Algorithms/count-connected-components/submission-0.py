class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build the adjacency list
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        visit = set()
        res = 0
        
        def dfs(i):
            visit.add(i)
            for neighbor in adj[i]:
                if neighbor not in visit:
                    dfs(neighbor)
                    
        # Step 2: Traverse every node to find all connected components
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
                
        return res