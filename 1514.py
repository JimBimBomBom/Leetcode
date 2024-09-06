import math

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        edgeDict = [[] for _ in range(n)]
        for i in range(len(edges)):
            if succProb[i] == 0:
                continue
            edgeDict[edges[i][0]].append((edges[i][1], math.log(succProb[i])))
            edgeDict[edges[i][1]].append((edges[i][0], math.log(succProb[i])))
        
        stack = [(math.log(1), start_node, set())]
        maxProb = 0
        while stack:
            prob, node, visited = stack.pop()
            visited.add(node)
            if node == end_node:
                maxProb = math.exp(prob)
                break

            for edge in edgeDict[node]:
                if edge[0] in visited:
                    continue
                stack.append((prob + edge[1], edge[0], visited))
            stack.sort()

        return maxProb
