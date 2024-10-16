# https://neetcode.io/problems/binary-tree-right-side-view
# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = []

        res = []
        if root:
            queue.append(root)

        while queue:
            newqueue = []
            for i in queue:
                if i.left:
                    newqueue.append(i.left)
                if i.right:
                    newqueue.append(i.right)
            res.append(queue[-1].val)
            queue = newqueue
        return res