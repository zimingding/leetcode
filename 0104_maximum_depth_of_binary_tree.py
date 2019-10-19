from TreeNode import TreeNode


class Solution:
    def __init__(self):
        self.maxD = 0

    def maxDepth(self, root: TreeNode) -> int:
        self.maxDepth_r(root, 0)
        return self.maxD

    def maxDepth_r(self, root: TreeNode, d: int):
        if root:
            d += 1
            if self.maxD < d:
                self.maxD = d
            if root.left:
                self.maxDepth_r(root.left, d)
            if root.right:
                self.maxDepth_r(root.right, d)
