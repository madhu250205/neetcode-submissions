from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # Stores indices of elements
        l = r = 0

        while r < len(nums):
            # 1. Pop smaller values from the back as they are useless
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # 2. Remove the left index if it falls outside the current window
            if l > q[0]:
                q.popleft()

            # 3. Once the window reaches size k, record the max and slide left
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1

        return output    