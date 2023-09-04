class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = dict()
        node = head
        while(node):
            if node in dic:
                return True
            dic[node] = True
            node = node.next
        return False