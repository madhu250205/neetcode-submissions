import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python only has min-heap, so we invert values to simulate a max-heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)  # Heaviest stone (most negative)
            second = heapq.heappop(stones) # Second heaviest stone
            
            if first != second:
                # Since values are negative, first - second results in the difference pushed back
                heapq.heappush(stones, first - second)
                
        stones.append(0)  # Handle case where all stones are destroyed (empty list)
        return abs(stones[0])