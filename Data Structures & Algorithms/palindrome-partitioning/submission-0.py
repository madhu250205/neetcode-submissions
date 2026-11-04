class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            # Base case: if we've reached the end of the string, record the valid partition
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                # Check if the current substring s[i:j+1] is a palindrome
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)  # Explore further partitions from the next index
                    part.pop()  # Backtrack

        dfs(0)
        return res

    def isPali(self, s: str, l: int, r: int) -> bool:
        # Helper function to check if a substring is a palindrome
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True