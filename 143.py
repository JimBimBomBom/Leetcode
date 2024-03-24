# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        listRepresentation = []
        while head:
            listRepresentation.append(head)
            head = head.next
        
        size = len(listRepresentation)
        leftIndex = 0
        rightIndex = size - 1

        while leftIndex < rightIndex:
            listRepresentation[leftIndex].next = listRepresentation[rightIndex]
            leftIndex += 1

            if leftIndex == rightIndex:
                break

            listRepresentation[rightIndex].next = listRepresentation[leftIndex]
            rightIndex -= 1

        listRepresentation[leftIndex].next = None
