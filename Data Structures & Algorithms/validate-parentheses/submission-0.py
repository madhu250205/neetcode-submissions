class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Hash map to pair closing brackets with their matching opening brackets
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                # If stack has elements and top matches expected opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                # Push opening bracket onto stack
                stack.append(c)

        # Valid only if stack is empty at the end
        return True if not stack else False