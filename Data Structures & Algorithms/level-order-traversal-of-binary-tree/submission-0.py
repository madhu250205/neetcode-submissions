from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        if root:
            q.append(root)

        while q:
            level_vals = []
            queue_len = len(q)

            # Process all nodes currently at this specific level
            for i in range(queue_len):
                node = q.popleft()
                level_vals.append(node.val)
                
                # Add children for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(level_vals)

        return res