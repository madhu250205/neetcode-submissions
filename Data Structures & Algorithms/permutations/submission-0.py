class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # Base case: if there's only 1 element, return it as a valid permutation
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            # Remove the first element (or current element)
            n = nums.pop(0)
            
            # Find all permutations of the remaining elements
            perms = self.permute(nums)
            
            # Append the removed element back to the end of each sub-permutation
            for p in perms:
                p.append(n)
                
            # Add them to our master results list
            res.extend(perms)
            
            # Backtrack: put the element back so the next iteration starts fresh
            nums.append(n)
            
        return res