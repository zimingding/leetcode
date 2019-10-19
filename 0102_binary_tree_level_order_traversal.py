from typing import List

from TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if root:
            levels.append(root)
        res = []
        while levels:
            copy = levels.copy()
            levels.clear()
            level = []
            for node in copy:
                level.append(node.val)
                if node.left:
                    levels.append(node.left)
                if node.right:
                    levels.append(node.right)
            res.append(level)
        return res
