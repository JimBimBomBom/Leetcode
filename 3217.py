class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        result = head
        nums = set(nums)
        start = -1
        end = start

        itterator = head
        while itterator:
            el = itterator
            if el.val in nums:
                end = el.next
            else:
                if start != end:
                    if start == -1:
                        result = end
                        start = end
                    else:
                        start.next = end
                        start = end
                else:
                    start = el
                    end = start
            itterator = itterator.next
        
        if start != end:
            start.next = None
                    
        return result
        