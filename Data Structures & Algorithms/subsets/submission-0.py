class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(i):
            # Base case: when we've considered all numbers, save a copy of the subset
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Decision 1: INCLUDE nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # Decision 2: EXCLUDE nums[i] (Backtrack)
            subset.pop()
            dfs(i + 1)
            
        dfs(0)
        return res