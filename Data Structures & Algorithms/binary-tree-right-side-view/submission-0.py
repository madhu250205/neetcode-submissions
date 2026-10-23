from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root] if root else [])

        while q:
            right_val = None
            q_len = len(q)

            for i in range(q_len):
                node = q.popleft()
                if node:
                    # Keep updating with the latest node seen on this level
                    right_val = node.val
                    
                    # Add child nodes to the queue for the next level
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            if right_val is not None:
                res.append(right_val)

        return res