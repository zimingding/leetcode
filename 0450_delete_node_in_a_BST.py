from TreeNode import TreeNode


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        pp = None
        curr = root
        while curr:
            if curr.val == key:
                break
            elif curr.val < key:
                pp = curr
                curr = curr.right
            else:
                pp = curr
                curr = curr.left

        if not curr:
            return root

        if not curr.left and not curr.right:
            if not pp:
                root = None
            elif pp.left and pp.left.val == key:
                pp.left = None
            else:
                pp.right = None
            return root

        if not curr.left:
            if not pp:
                root = curr.right
            elif pp.left and pp.left.val == key:
                pp.left = curr.right
            else:
                pp.right = curr.right
            return root

        if not curr.right:
            if not pp:
                root = curr.left
            elif pp.left and pp.left.val == key:
                pp.left = curr.left
            else:
                pp.right = curr.left
            return root

        # find minimum node in right hand side
        dummy = curr
        right = curr.right
        while right.left:
            dummy = right
            right = right.left

        if dummy.left == right:
            dummy.left = right.right
        else:
            dummy.right = right.right
        curr.val = right.val

        return root
