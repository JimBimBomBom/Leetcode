class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        def findPath(currSource, edges, destination):
            while True:
                availableEdges = set([element for edge in edges if edge[0] == currSource or edge[1] == currSource for element in edge])
                # print("Curr test", currSource, availableEdges)
                availableEdges.discard(currSource)

                if destination in availableEdges:
                    # print("Found destination")
                    return True
                else:
                    if len(availableEdges) == 0:
                        # print("No available edges")
                        break
                    else:
                        # print("Going to next source")
                        for newSource in availableEdges:
                            # print("Trying", newSource)
                            if(findPath(newSource, [edge for edge in edges if edge[0] != currSource and edge[1] != currSource], destination)):
                                return True
                return False
        
        return findPath(source, edges, destination)
        