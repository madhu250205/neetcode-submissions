# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            # If both nodes are greater than current, go right
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both nodes are smaller than current, go left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # Otherwise, we found the split point (the LCA)
            else:
                return curr