from listnode import ListNode


class Solution:
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

