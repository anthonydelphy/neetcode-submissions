# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseList(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        # Only one value edge case
        if head.next is None and n == 1:
            return None

        temp = reverseList(head)
        temp1 = temp
        if n == 1:
            return reverseList(temp.next)

        temp2 = temp.next
        while n > 2:
            n -= 1
            temp1 = temp1.next
            temp2 = temp2.next


        temp1.next = temp2.next
        return reverseList(temp)


        
            

        