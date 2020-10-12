class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        front, last = head, head
        for i in range(1, k+1):
            front = front.next
        while (front != None):
            front = front.next
            last = last.next
        return last
