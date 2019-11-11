# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from listnode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # if m == n == 1:
        #     return head

        prev = None
        curr = head
        ne = curr.next
        i = 1
        while i < n:
            if i < m:
                prev = curr
            curr = curr.next
            ne = curr.next
            i += 1

        dummy = None
        if not prev:
            q = head
        else:
            q = prev.next
        while q is not ne:
            temp = q.next
            q.next = dummy
            dummy = q
            q = temp

        if not prev and not ne:
            return dummy

        if not prev:
            head.next = ne
            return dummy
        else:
            t2 = prev.next
            prev.next = dummy
            t2.next = ne
            return head



head = ListNode(3)
head.next = ListNode(5)
#head.next.next = ListNode(4)
node = Solution().reverseBetween(head, 1, 2)
print(node)