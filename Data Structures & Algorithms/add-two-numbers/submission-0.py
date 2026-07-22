# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        def convertList(head):
            temp = head
            l1Sum = head.val
            i = 1
            while temp.next:
                temp = temp.next
                l1Sum += (temp.val * (10**i))
                i +=1
            return l1Sum

        def strToList(input):
            if len(input) == 1:
                return ListNode(val = int(input))
            newList = ListNode()
            temp = newList         
            for i in range(len(input)):
                temp.val = int(input[i])
                if i != len(input)-1:
                    temp.next = ListNode()
                    temp = temp.next
            return newList

        listSums = convertList(l1) + convertList(l2)    
        return strToList(str(listSums)[::-1])