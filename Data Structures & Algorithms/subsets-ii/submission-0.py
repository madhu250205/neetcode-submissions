class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort to group duplicates together
        
        def backtrack(i, subset):
            # Base case: when we've considered all elements, record the subset
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Decision 1: INCLUDE nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            
            # Decision 2: EXCLUDE nums[i] and skip all subsequent duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
            
        backtrack(0, [])
        return res