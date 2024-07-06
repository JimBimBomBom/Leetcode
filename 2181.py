class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head
        resultStart = result
        sum = 0

        while head:
            if head.val == 0:
                if sum > 0:
                    result.val = sum
                    sum = 0
                    if head.next:
                        result = result.next
                    else:
                        result.next = None
                        break
            else:
                sum += head.val
            head = head.next
        
        return resultStart
