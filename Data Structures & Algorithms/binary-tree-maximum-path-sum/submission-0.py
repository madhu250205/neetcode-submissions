# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            
            # Ignore negative sums from subtrees by taking max with 0
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            # Compute the max path sum with the current node acting as the highest peak
            res[0] = max(res[0], node.val + left_max + right_max)
            
            # Return the max sum of a single path extending upwards to the parent
            return node.val + max(left_max, right_max)

        dfs(root)
        return res[0]