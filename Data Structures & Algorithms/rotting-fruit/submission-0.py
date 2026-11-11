from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        
        # Step 1: Count all fresh fruits and add initial rotten fruits to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
                    
        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # Step 2: BFS level-by-level (each level represents 1 minute)
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # Check boundaries and ensure the neighbor is a fresh fruit
                    if (row < 0 or row >= rows or 
                        col < 0 or col >= cols or 
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    fresh -= 1
                    queue.append((row, col))
            time += 1
            
        # Step 3: Return time if all fresh fruits are rotted, otherwise -1
        return time if fresh == 0 else -1