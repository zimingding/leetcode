from listnode import ListNode


class Solution(object):
    def hasCycle(self, head: ListNode) -> bool:
        s = head
        f = head
        while True:
            if not s or not s.next or not f.next:
                return False
            s = s.next

            f = f.next.next
            if not f:
                return False
            if s is f:
                return True


head = ListNode(1)
tail = ListNode(2)
head.next = tail
tail.next = head
print(Solution().hasCycle(head))
