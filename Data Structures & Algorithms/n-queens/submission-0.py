class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            # Base case: if we've successfully placed a queen in every row, record the board layout
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                # Check if the column or diagonals are already under attack
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # Place the queen
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Recurse to place a queen in the next row
                backtrack(r + 1)

                # Backtrack: remove the queen and clear the sets for alternative paths
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res