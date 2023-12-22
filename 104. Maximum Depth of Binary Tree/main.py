# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def util(tree):
            if not tree:
                return 0
            return 1 + max(util(tree.left),util(tree.right))
        return util(root)
