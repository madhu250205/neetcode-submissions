class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        
        def dfs(r, c):
            # Base case: check boundaries and water cells
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                grid[r][c] == 0):
                return 0
            
            # Mark the cell as visited by changing it to 0 (sinking it)
            grid[r][c] = 0
            
            # Count the current cell (1) plus all connected land cells in 4 directions
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) + 
                        dfs(r, c - 1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Update max_area with the size of the discovered island
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area