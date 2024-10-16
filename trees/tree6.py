# https://neetcode.io/problems/kth-smallest-integer-in-bst
# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        cur = root
        stack.append(root)
        prev = None
        while k:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            prev = cur
            cur = cur.right
        
        return prev.val