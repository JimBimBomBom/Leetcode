# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        list_parts = [None]*k
        node = head
        count = 0
        while(node):
            count += 1
            node = node.next
        parts_len = [count//k + (1 if idx < count%k else 0) for idx in range(k)]
        
        node = head
        count = 0
        index = 0
        while(node):
            decouple_node = None
            if count == 0:
                list_parts[index] = node
            count += 1
            if count == parts_len[index]:
                decouple_node = node
                count = 0
                index += 1
            node = node.next
            if decouple_node:
                decouple_node.next = None

        return list_parts