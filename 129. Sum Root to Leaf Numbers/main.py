# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def util(tree,curr):
            if not tree:
                return
            curr = curr*10 + tree.val
            if not tree.left and not tree.right:
                self.ans += curr
                return
            util(tree.left,curr)
            util(tree.right,curr)
        util(root,0)
        return self.ans