# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cutStart = None
        cutEnd = None

        index = 0
        curr = list1
        while curr.next:
            if index == a - 1:
                cutStart = curr
            if index == b:
                cutEnd = curr
                break
            index += 1
            curr = curr.next

        cutStart.next = list2

        curr2 = list2
        while curr2.next:
            curr2 = curr2.next
        
        curr2.next = cutEnd.next

        return list1
        