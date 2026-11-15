from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        count = Counter(tasks)
        # Max-heap to store task frequencies (inverted for Python's min-heap)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        # Queue stores pairs of [cnt, idle_time_when_available]
        q = deque() 
        
        while maxHeap or q:
            time += 1
            
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1  # Execute task (increment because negative)
                if cnt != 0:
                    q.append([cnt, time + n])     # Send to cooldown queue
                    
            # Check if any task has finished its cooldown
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time