# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        self.maxh = 0
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def util(tree,h):
            if not tree:
                return
            if h>self.maxh:
                self.ans.append(tree.val)
                self.maxh = h
            util(tree.right,h+1)
            util(tree.left,h+1)
        util(root,1)
        return self.ans

        