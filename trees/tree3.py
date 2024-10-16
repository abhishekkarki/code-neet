# https://neetcode.io/problems/level-order-traversal-of-binary-tree
# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        res = []
        resdict = defaultdict(list)
        def dfs(node, i):
            if not node:
                return
            resdict[i].append(node.val)
            dfs(node.left, i+1)
            dfs(node.right, i+1)
        dfs(root, 1)

        for key, val in resdict.items():
            res.append(val)
        
        return res

# Solution 2
# better
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        if root:
            q.append(root)

        while q:
            val = []
            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res
