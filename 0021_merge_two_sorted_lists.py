from listnode import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = None
        curr = None
        first = True
        while l1 is not None or l2 is not None:
            n = 0
            if l1 is None:
                n = l2.val
                l2 = l2.next
            elif l2 is None:
                n = l1.val
                l1 = l1.next
            elif l1.val < l2.val:
                n = l1.val
                l1 = l1.next
            else:
                n = l2.val
                l2 = l2.next
            if first:
                res = ListNode(n)
                curr = res
                first = False
            else:
                curr.next = ListNode(n)
                curr = curr.next
        return res
