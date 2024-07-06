class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        result = 0
        dict = {}
        for road in roads:
            if road[0] not in dict:
                dict[road[0]] = 0
            if road[1] not in dict:
                dict[road[1]] = 0
            dict[road[0]] += 1
            dict[road[1]] += 1

        i = n
        for value in sorted(dict.values(), key=lambda x: x, reverse=True):
            result += value*i
            i -= 1
        
        return result
            