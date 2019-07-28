from listnode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


    # my lengthy solution that do two nodes at once
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next = curr.next
            if next:
                curr.next = prev
                temp = next.next
                next.next = curr
                curr = temp
                prev = next
            else:
                curr.next = prev
                return curr

        return prev


four = ListNode(4)
three = ListNode(3)
two = ListNode(2)
one = ListNode(1)
one.next = two
two.next = three
three.next = four

head = Solution().reverseList(one)
print(head.val)
