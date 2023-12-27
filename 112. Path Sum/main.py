# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def util(tree,target):
            if not tree:
                return False
            if not tree.left and not tree.right:
                return tree.val == target
            return util(tree.left,target-tree.val) or util(tree.right,target-tree.val)
        return util(root,targetSum)
        