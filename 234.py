# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        listRepresentation = []

        while head:
            listRepresentation.append(head)
            head = head.next
        
        size = len(listRepresentation)
        for i in range(size//2):
            if listRepresentation[i].val != listRepresentation[size - i - 1].val:
                return False
        return True
        


        