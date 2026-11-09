class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # Base case: check boundaries and water cells
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                grid[r][c] == "0"):
                return
            
            # Sink the land cell to mark it as visited
            grid[r][c] = "0"
            
            # Recursively explore all 4 neighboring directions (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                # When we find a piece of land, we found a new island
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands