from typing import List

from TreeNode import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        nodes = []
        if root:
            nodes.append(root)
        from_left = True
        while nodes:
            level = []
            l_nodes = []
            for node in nodes:
                level.append(node.val)
                if node.left:
                    l_nodes.append(node.left)
                if node.right:
                    l_nodes.append(node.right)
            if from_left:
                level.reverse()
                from_left = not from_left
            res.append(level)
            nodes = l_nodes
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

res = Solution().zigzagLevelOrder(root)
print(res)
