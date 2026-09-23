class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # If duplicate character found, shrink window from left
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            # Add current character to set and update max length
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res