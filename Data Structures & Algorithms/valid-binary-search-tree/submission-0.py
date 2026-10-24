# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low, high):
            # Base case: an empty node is valid
            if not node:
                return True
            
            # The current node's value must strictly fit within the allowed range
            if not (low < node.val < high):
                return False
            
            # Recursively validate left and right subtrees with updated boundaries
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))

        return validate(root, float("-inf"), float("inf"))