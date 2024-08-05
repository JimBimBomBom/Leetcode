class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        result = ""
        dictionary = {}
        for index in range(len(arr)):
            if arr[index] not in dictionary:
                dictionary[arr[index]] = (index, 1)
            else:
                dictionary[arr[index]] = (0, dictionary[arr[index]][1] + 1) #once the element occurs more than once, it is of no interest to us
        
        for key in sorted([el for el in dictionary if dictionary[el][1] == 1], key = lambda x: dictionary[x][0]):
            if k == 1:
                result = key
                break
            k -= 1
        
        return result
        