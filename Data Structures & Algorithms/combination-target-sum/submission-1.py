class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # Base case: if we hit the exact target, save a copy of our combination
            if total == target:
                res.append(cur.copy())
                return
            
            # Base case: if we exceed the target or go out of bounds, stop exploring this path
            if i >= len(nums) or total > target:
                return

            # Decision 1: Include nums[i] (we can reuse it, so we keep index 'i')
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()

            # Decision 2: Exclude nums[i] and move on to the next element (index 'i + 1')
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res