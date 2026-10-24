# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value in inorder to its index for O(1) lookups
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        
        self.pre_idx = 0
        
        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            # The current root is the next element in preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            # Find the root's position in inorder to split left and right subtrees
            mid = inorder_idx[root_val]
            
            # Recursively build left and right branches
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
            
        return helper(0, len(inorder) - 1)