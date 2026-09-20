class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            # Calculate current water area
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            # Shift the pointer pointing to the shorter height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res