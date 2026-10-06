class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, (ROWS * COLS) - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // COLS
            col = mid % COLS

            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
        