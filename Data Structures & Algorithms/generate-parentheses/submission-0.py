class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def backtrack(openN: int, closedN: int):
            # Base case: if we've used 'n' open and 'n' closed parentheses, we have a valid combination
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            # Choice 1: Add an open parenthesis if we haven't reached n yet
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
                
            # Choice 2: Add a closing parenthesis if there are unmatched open parentheses
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
                
        backtrack(0, 0)
        return res