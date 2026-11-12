class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
            
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prev_height):
            # Check boundaries, visited set, and whether water can flow uphill
            if ((r, c) in visit or 
                r < 0 or c < 0 or 
                r == rows or c == cols or 
                heights[r][c] < prev_height):
                return
                
            visit.add((r, c))
            # Explore all 4 orthogonal directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            
        # Step 1: Run DFS from Pacific borders (top row and left column)
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            
        # Step 2: Run DFS from Atlantic borders (bottom row and right column)
        for c in range(cols):
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, cols - 1, atl, heights[r][cols - 1])
            
        # Step 3: Find cells that can reach both oceans
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
                    
        return res