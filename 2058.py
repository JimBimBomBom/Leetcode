class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = [-1, -1]
        if not head.next:
            return result

        lastNode = head
        thisNode = head
        nextNode = head.next
        index = 0
        lastIndex = 0

        while head:
            if not nextNode.next:
                break
            lastNode = thisNode
            thisNode = thisNode.next
            nextNode = nextNode.next
            index += 1

            if (lastNode.val < thisNode.val and thisNode.val > nextNode.val) or (lastNode.val > thisNode.val and thisNode.val < nextNode.val):
                if lastIndex != 0:
                    if result[1] == -1:
                        result[1] = index - lastIndex
                    else:
                        result[1] += index - lastIndex
                    if result[0] == -1:
                        result[0] = index - lastIndex
                    else:
                        result[0] = min(result[0], index - lastIndex)

                lastIndex = index

        return result
        