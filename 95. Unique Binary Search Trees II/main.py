# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def util(start,end):
            if end == start:
                return [TreeNode(val=start)]
            elif end<start:
                return [None]
            bstlist = []
            for i in range(start,end+1):
                left_trees = util(start,i-1)
                right_trees = util(i+1,end)
                for left in left_trees:
                    for right in right_trees:
                        curr_tree = TreeNode(val=i,left = left,right=right)
                        bstlist.append(curr_tree)
            return bstlist
        return util(1,n)
        