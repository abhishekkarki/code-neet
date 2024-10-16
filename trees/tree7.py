# https://neetcode.io/problems/serialize-and-deserialize-binary-tree
# Hard

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serial_list = []
        def dfs_serial(node):
            if not node:
                serial_list.append('null')
            else:
                serial_list.append(node.val)
                dfs_serial(node.left)
                dfs_serial(node.right)
            return
        
        dfs_serial(root)

        return ','.join([str(i) for i in serial_list])

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        from collections import deque
        serial_list = deque(data.split(','))

        # while serial_list:
        #     val = serial_list.popleft()
        #     cur
        def dfs_deserial():
            if not serial_list:
                return None
            val = serial_list.popleft()
            if val == 'null':
                return None
            else:
                root = TreeNode(val)
                root.left = dfs_deserial()
                root.right = dfs_deserial()
                return root
        
        return dfs_deserial()
