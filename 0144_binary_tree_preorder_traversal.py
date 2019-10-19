from typing import List

import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.preorderTraversal_r(root, res)
        return res

    def preorderTraversal_r(self, root: TreeNode, res: List[int]):
        if root:
            res.append(root.val)
            self.preorderTraversal_r(root.left, res)
            self.preorderTraversal_r(root.right, res)
