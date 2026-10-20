# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            # Base case: an empty tree is balanced and has height 0
            if not node:
                return [True, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Current node is balanced if left/right are balanced and height diff <= 1
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            
            # Return balance status and calculate current height
            height = 1 + max(left[1], right[1])
            return [balanced, height]
        
        return dfs(root)[0]