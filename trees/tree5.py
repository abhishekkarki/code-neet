# https://neetcode.io/problems/valid-binary-search-tree
# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        valid = True

        def dfs(node):
            nonlocal valid
            nodemin, nodemax = node.val, node.val
            if node.left:
                leftmin, leftmax = dfs(node.left)
                if leftmax >= node.val:
                    valid = False
                nodemin = leftmin
            if node.right:
                rightmin, rightmax = dfs(node.right)
                if rightmin <= node.val:
                    valid = False
                nodemax = rightmax
            return (nodemin, nodemax)
        dfs(root)
        return valid
            