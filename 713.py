class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        size = len(nums)
        product = 1
        leftIndex = 0
        rightIndex = 0
        oldRightIndex = 0
        result = 0

        while leftIndex <= rightIndex and rightIndex < size:
            product *= nums[rightIndex]
            print(nums[rightIndex])
            if product >= k:
                print("product >= k")
                print(product)

                elementsInSubarray = rightIndex - leftIndex
                print("result: " + str(result))
                for i in range(1, elementsInSubarray + 1):
                    result += i
                print("new result: " + str(result))

                if oldRightIndex >= leftIndex:
                    commonElementsInSubarray = oldRightIndex - leftIndex
                    for i in range(1, commonElementsInSubarray + 1):
                        result -= i
                print("new adjusted result: " + str(result))

                oldRightIndex = rightIndex

                while leftIndex <= rightIndex and product >= k:
                    print("product >= k forloop")
                    product //= nums[leftIndex]
                    leftIndex += 1
                    print("leftIndex: " + str(leftIndex))
                    print("product: " + str(sum))
            rightIndex += 1
        
        if product < k:
            elementsInSubarray = rightIndex - leftIndex
            for i in range(elementsInSubarray + 1):
                result += i
            print("new result: " + str(result))
            if oldRightIndex >= leftIndex:
                commonElementsInSubarray = oldRightIndex - leftIndex
                for i in range(1, commonElementsInSubarray + 1):
                    result -= i
            print("new adjusted result: " + str(result))

        return result
        