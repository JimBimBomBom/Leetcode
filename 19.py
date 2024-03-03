# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        elementPointers = []

        curr = head
        elementPointers.append(curr)
        while curr.next != None:
            curr = curr.next
            elementPointers.append(curr)
        
        if len(elementPointers) == 1:
            return None
        
        removeIndex = len(elementPointers) - n
        if removeIndex == 0:
            return head.next
        else:
            elementPointers[removeIndex - 1].next = elementPointers[removeIndex].next
            return head
        