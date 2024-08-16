class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        numsElements = list(set(nums))
        numsElements.sort()
        # print("NumsElements: ", numsElements)   
        
        # here we reduce k by some value of duplicates in nums
        elementsCount = [0] * len(numsElements)
        for i in range(len(numsElements)):
            elCount = nums.count(numsElements[i])
            elementsCount[i] = elCount
            if elCount > 1:
                k -= (elCount * (elCount - 1)) // 2
                if k <= 0:
                    return 0
        # print("Reduced k: ", k)

        distArray = list()
        count = 0
        distArray = sorted(distArray, key=lambda x: x[0])
        # print("DistArray: ", distArray) 
        for i in range(1, len(numsElements)):
            changeHappened = False
            for j in range(0, len(numsElements) - i):
                if count < k:
                    changeHappened = True
                    distArray.append((abs(numsElements[j] - numsElements[j + i]), elementsCount[j] * elementsCount[j + i]))
                    count += elementsCount[j] * elementsCount[j + i]
                    if count >= k:
                        distArray.sort()
                else:
                    # print("J: ", j)
                    # print("I: ", j + i)
                    if distArray[-1][0] > abs(numsElements[j] - numsElements[j + i]):
                        # print(numsElements[j], numsElements[j + i], "is better than", distArray[-1][0])
                        changeHappened = True
                        distArray.append((abs(numsElements[j] - numsElements[j + i]), elementsCount[j] * elementsCount[j + i]))
                        count += elementsCount[j] * elementsCount[j + i]
                        distArray.sort()
                        while (count - distArray[-1][1]) >= k:
                            popped = distArray.pop()
                            count -= popped[1]
            
            if not changeHappened:
                # print("here")
                # print("DistArray: ", distArray)
                break
        if not distArray:
            return 0

        return distArray[-1][0]
