from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store the grouped anagrams, mapping a count tuple to a list of strings
        res = defaultdict(list)
        for s in strs:
            # Count the frequency of each character (a-z)
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Use the tuple of counts as the key since lists are unhashable
            res[tuple(count)].append(s)
            
        return list(res.values())        