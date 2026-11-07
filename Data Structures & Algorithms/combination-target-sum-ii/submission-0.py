class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(cur, pos, target):
            if target == 0:
                res.append(list(cur))
                return
            if target < 0:
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                # Skip duplicates at the same branch level
                if candidates[i] == prev:
                    continue
                
                cur.append(candidates[i])
                # i + 1 ensures each element is used at most once
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                
                prev = candidates[i]
                
        backtrack([], 0, target)
        return res