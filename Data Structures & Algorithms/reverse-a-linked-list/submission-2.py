# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        temp = head
        i = []
        while temp is not None:
            print(temp.val)
            i.append(temp.val)
            temp = temp.next
        i.reverse()
        result = ListNode()
        tmp = result
        for x,y in enumerate(i):
            print(y)
            result.val = y
            if x < len(i)-1:
                result.next = ListNode()
                result = result.next
            
        return tmp