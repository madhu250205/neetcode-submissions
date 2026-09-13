class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i
            # Find the position of the delimiter '#'
            while s[j] != "#":
                j += 1
            
            # Extract string length
            length = int(s[i:j])
            
            # Extract the actual string using the length
            i = j + 1
            j = i + length
            res.append(s[i:j])
            
            # Move index to the start of the next encoded string
            i = j
            
        return res