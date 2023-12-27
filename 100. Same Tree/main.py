# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def util(first,second):
            if not first or not second:
                return not(first or second)
            if first.val == second.val:
                return util(first.left,second.left) and util(first.right,second.right)
            else:
                return False
        return util(p,q)
        