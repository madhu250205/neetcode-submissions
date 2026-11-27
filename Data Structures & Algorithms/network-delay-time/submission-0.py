import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build the adjacency list mapping source to (target, time)
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
            
        # Step 2: Initialize min-heap with (current_time, node) starting at k
        minHeap = [(0, k)]
        visit = set()
        t = 0
        
        # Step 3: Dijkstra's Algorithm traversal
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)
            
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
                    
        # Return max time if all nodes were reached, otherwise -1
        return t if len(visit) == n else -1
        