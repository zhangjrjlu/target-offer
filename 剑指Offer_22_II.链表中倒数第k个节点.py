class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        front, last = head, head
        for i in range(1, k+1):
            front = front.next
        while (front != None):
            front = front.next
            last = last.next
        return last
        class Solution:
    
#         n = 0
#         f = head
#         l = head
#         while f:
#             f = f.next
#             n = n+1
#         print (n)
#         for i in range(n-k):
#             l = l.next
#         return l
    
        # former, latter = head, head
        # for _ in range(k):
        #     former = former.next
        # while former:
        #     former, latter = former.next, latter.next
        # return latter

