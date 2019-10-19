from typing import List

import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.postorderTraversal_r(root, res)
        return res

    def postorderTraversal_r(self, root: TreeNode, res: List[int]):
        if root:
            self.postorderTraversal_r(root.left, res)
            self.postorderTraversal_r(root.right, res)
            res.append(root.val)
