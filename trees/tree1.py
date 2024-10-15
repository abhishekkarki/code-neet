# tree code 1
# level: easy
# link: https://neetcode.io/problems/subtree-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root:
            return False
        elif not subRoot:
            return False
        elif root.val == subRoot.val:
            if self.sametree(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def sametree(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif not root:
            return False
        elif not subRoot:
            return False
        elif root.val == subRoot.val:
            return self.sametree(root.left, subRoot.left) and self.sametree(root.right, subRoot.right)
