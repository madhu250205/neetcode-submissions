class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        res = []
        digit_to_char = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        def backtrack(i, cur_str):
            # Base case: if our current string length matches the digits length, record it
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return
                
            # Iterate through all letters mapped to the current digit
            for char in digit_to_char[digits[i]]:
                backtrack(i + 1, cur_str + char)
                
        backtrack(0, "")
        return res