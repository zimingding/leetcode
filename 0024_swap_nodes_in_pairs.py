from listnode import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        if not curr or not curr.next:
            return head
        follow = curr.next
        curr.next = follow.next
        follow.next = curr
        dummy.next = follow
        head = dummy.next
        while curr.next and curr.next.next:
            dummy = curr
            curr = curr.next
            follow = curr.next
            curr.next = follow.next
            follow.next = curr
            dummy.next = follow
        return head


four = ListNode(4)
three = ListNode(3)
three.next = four
two = ListNode(2)
two.next = three
one = ListNode(1)
one.next = two
Solution().swapPairs(one)
