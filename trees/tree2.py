# https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree
# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        print(p.val, q.val)
        cur = root
        while True:
            if cur.val == p.val:
                return cur
            elif cur.val == q.val:
                return cur
            elif cur.val < p.val:
                cur = cur.right
            elif cur.val > q.val:
                cur = cur.left
            else:
                return cur
