# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next

        arr.reverse()
        print(arr)

        temp = head
        i = 0
        while temp.next:
            nxt = temp.next
            temp.next = ListNode()
            temp.next.next = nxt
            temp.next.val = arr[i]
            temp = temp.next.next
            i += 1
        
        temp = head
        i = 0

        while i < len(arr)-1:
            temp = temp.next
            i +=1

        temp.next = None
            

