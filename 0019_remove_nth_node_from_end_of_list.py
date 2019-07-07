from listnode import ListNode


class Solution:

    # Idea from solution
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        size = 1
        while curr.next is not None:
            curr = curr.next
            size += 1
        if size - n == 0:
            head = head.next
        else:
            curr = head
            while size - n - 1 > 0:
                curr = curr.next
                size -= 1
            if n == 1:
                curr.next = None
            else:
                curr.next = curr.next.next
        return head


    # extra memory to store the pointer
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodeList = []
        curr = head
        nodeList.append(curr)
        while curr.next is not None:
            curr = curr.next
            nodeList.append(curr)
        prev = -1*n - 1
        next = -1*n + 1
        if prev < -1 * len(nodeList):
            head = head.next
        elif next > -1:
            nodeList[prev].next = None
        else:
            nodeList[prev].next = nodeList[next]
        return head

