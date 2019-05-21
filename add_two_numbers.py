from listnode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        curr = res
        carry = 0
        first = True
        while l1 is not None or l2 is not None or carry == 1:
            a = 0 if l1 is None else l1.val
            b = 0 if l2 is None else l2.val
            c = (a + b + carry) % 10
            if first:
                curr.val = c
                first = False
            else:
                curr.next = ListNode(c)
                curr = curr.next
            carry = 1 if a + b + carry >= 10 else 0
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return res


a = ListNode(9)
a.next = ListNode(9)
b = ListNode(1)
c = Solution().addTwoNumbers(a, b)
while c is not None:
    print(c.val)
    c = c.next
