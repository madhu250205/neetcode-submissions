import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # Check for duplicates in current row, column, or 3x3 sub-box
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[(r // 3, c // 3)]):
                    return False
                
                # Add value to respective sets
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)

        return True
        