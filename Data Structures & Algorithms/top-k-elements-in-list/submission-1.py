class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # Create buckets where index = frequency
        freq = [[] for _ in range(len(nums) + 1)]
        
        # 1. Count occurrences of each number
        for n in nums:
            count[n] = 1 + count.get(n,0)
            
        # 2. Group numbers by their frequency
        for n, c in count.items():
            freq[c].append(n)
            
        # 3. Gather the top k elements starting from highest frequency
        res = []
        for i in range(len(freq) - 1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res       