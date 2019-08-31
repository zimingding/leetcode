from typing import List
from listnode import ListNode

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        for list in lists:
            while list:
                nodes.append(list.val)
                list = list.next
        head = point = ListNode(-1)
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = None
        for l in lists:
            head = self.mergeList(head, l)
        return head

    def mergeList(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next
