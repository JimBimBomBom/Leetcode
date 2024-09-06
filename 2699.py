class Solution:
    pathStack = []

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        edgeDict = {}
        for edge in edges:
            if edge[0] not in edgeDict:
                edgeDict[edge[0]] = []
            edgeDict[edge[0]].append((edge[1], edge[2]))

            if edge[1] not in edgeDict:
                edgeDict[edge[1]] = []
            edgeDict[edge[1]].append((edge[0], edge[2]))
        
        print(edgeDict)
        
        def dfs(node, weight, unknownEdges):
            result = []
            if node == destination and weight == target:
                return self.pathStack
            for edge in edgeDict[node]:
                if edge[1] == -1:
                    if (weight + 1) <= target:
                        self.pathStack.append((node, edge[0], edge[1]))
                        result = dfs(edge[0], weight + 1, unknownEdges + 1)
                        self.pathStack.pop()
                        if result != []:
                            return result
                elif (weight + edge[1]) <= target:
                    self.pathStack.append((node, edge[0], edge[1]))
                    result = dfs(edge[0], weight + edge[1], unknownEdges)
                    self.pathStack.pop()
                    if result != []:
                        return result
            print(self.pathStack)
            return result

        dfs(source, 0, 0)

        return self.pathStack
        