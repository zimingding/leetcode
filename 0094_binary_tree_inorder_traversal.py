from typing import List
import TreeNode


class Solution:
    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.inorder_r(root)
        return self.res

    def inorder_r(self, node: TreeNode):
        if node:
            self.inorder_r(node.left)
            self.res.append(node.val)
            self.inorder_r(node.right)
