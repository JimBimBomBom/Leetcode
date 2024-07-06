class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        dict = {}

        for edge in edges:
            if edge[1] not in dict:
                dict[edge[1]] = set()
            dict[edge[1]].add(edge[0])
        
        # print(dict)
        
        result = [list() for _ in range(n)]
        for key, value in sorted(dict.items(), lambda x: x[0]):
            for aKey in list(value):
                if aKey not in dict:
                    continue
                # print(aKey)
                dict[key] = dict[key].union(dict[aKey])
            result[key] = (sorted(list(dict[key])))
        
        # print(result)

        return result
