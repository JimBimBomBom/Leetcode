def unifySet(subsets):
    for subsetIndex in range(len(subsets)):
        doBreak = False
        for offsetSubsetIndex in range(subsetIndex + 1, len(subsets)):
            if subsets[subsetIndex].intersection(subsets[offsetSubsetIndex]):
                subsets[subsetIndex] = subsets[subsetIndex].union(subsets[offsetSubsetIndex])
                subsets.pop(offsetSubsetIndex)
                doBreak = True
                break
        if doBreak:
            break
    

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0

        initialEdgeCount = len(edges)
        edges = list(set((edge[0], edge[1], edge[2]) for edge in edges)) # remove duplicates
        result = initialEdgeCount - len(edges)

        subsets = []
        edges.sort(key=lambda x: x[0], reverse=True)
        knownPoints = set()
        while True:
            if not edges:
                break
            if edges[0][0] == 3:
                edge = edges.pop(0)
                subset = set()
                subset.add(edge[1])
                knownPoints.add(edge[1])
                subset.add(edge[2])
                knownPoints.add(edge[2])
                for edge2 in edges:
                    if edge2[0] == 3:
                        if edge2[1] in subset:
                            knownPoints.add(edge2[2])
                            subset.add(edge2[2])
                            edges.remove(edge2)
                        elif edge2[2] in subset:
                            knownPoints.add(edge2[1])
                            subset.add(edge2[1])
                            edges.remove(edge2)
                    else:
                        break
                subsets.append(subset) # append largest connected subset
            else:
                break
        initialEdgeCount = len(edges)
        # edges = list(filter(lambda x: (x[1] not in knownPoints or x[2] not in knownPoints), edges))
        for subset in subsets:
            edges = list(filter(lambda x: (x[1] not in subset or x[2] not in subset), edges))
        print("Old result: " + str(result)) 
        result += initialEdgeCount - len(edges)
        print("New result: " + str(result)) 

        print(edges)
        print("Len: " + str(len(edges))) 
        if len(list(knownPoints)) == n and len(subsets) == 1:
            return result
        elif len(edges) == 0:
            return -1

        # add path A 
        pathA = subsets
        if not pathA:
            pathA = [set([1])]

        knownPointsA = knownPoints.copy()
        if not knownPointsA:
            knownPointsA.add(1)

        edgesA = list(filter(lambda x: x[0] == 2, edges))

        print("Initial A: ")
        print(pathA)
        print(knownPointsA)
        print(edgesA)
        while True:
            addedNew = False
            for subsetA in pathA:
                doBreak = False
                edgesForSubset = list(filter(lambda x: x[1] in subsetA or x[2] in subsetA, edgesA))
                if len(edgesForSubset) != 0:
                    addedNew = True
                else:
                    continue

                for edge in edgesForSubset:
                    if edge[1] in knownPointsA and edge[2] in knownPointsA:
                        subsetA.add(edge[1])
                        subsetA.add(edge[2])
                        edgesA.remove(edge)
                        # perform a union of the two subsets
                        doBreak = True
                        break
                    elif edge[1] in subsetA:
                        subsetA.add(edge[2])
                        knownPointsA.add(edge[2])
                        edgesA.remove(edge)
                    elif edge[2] in subsetA:
                        subsetA.add(edge[1])
                        knownPointsA.add(edge[1])
                        edgesA.remove(edge)
                if doBreak:
                    break
                
            for subsetIndex in range(len(pathA)):
                doBreak = False
                for offsetSubsetIndex in range(subsetIndex + 1, len(pathA)):
                    if pathA[subsetIndex].intersection(pathA[offsetSubsetIndex]):
                        pathA[subsetIndex] = pathA[subsetIndex].union(pathA[offsetSubsetIndex])
                        pathA.pop(offsetSubsetIndex)
                        doBreak = True
                        break
                if doBreak:
                    break

            print("New A: ")
            print(pathA)
            print(knownPointsA)
            print(edgesA)

            if len(list(knownPointsA)) == n:
                print("Old result: " + str(result))
                print(edgesA)
                result += len(edgesA) # add remaining edges
                print("New result: " + str(result))
                break
            elif len(edgesA) == 0 or not addedNew:
                return -1

        # add path B 
        pathB = subsets
        if not pathB:
            pathB = [set([1])]

        knownPointsB = knownPoints.copy()
        if not knownPointsB:
            knownPointsB.add(1)
        edgesB = list(filter(lambda x: x[0] == 1, edges))

        print("Initial B: ")
        print(pathB)
        print(knownPointsB)
        print(edgesB)
        while True:
            addedNew = False
            for subsetB in pathB:
                edgesForSubset = list(filter(lambda x: x[1] in subsetB or x[2] in subsetB, edgesB))
                if len(edgesForSubset) != 0:
                    addedNew = True
                else:
                    continue

                for edge in edgesForSubset:
                    if edge[1] in knownPointsB and edge[2] in knownPointsB:
                        subsetB.add(edge[1])
                        subsetB.add(edge[2])
                        edgesB.remove(edge)
                        # perform a union of the two subsets
                        break
                    elif edge[1] in subsetB:
                        subsetB.add(edge[2])
                        knownPointsB.add(edge[2])
                        edgesB.remove(edge)
                    elif edge[2] in subsetB:
                        subsetB.add(edge[1])
                        knownPointsB.add(edge[1])
                        edgesB.remove(edge)
                
            for subsetIndex in range(len(pathB)):
                doBreak = False
                for offsetSubsetIndex in range(subsetIndex + 1, len(pathB)):
                    if pathB[subsetIndex].intersection(pathB[offsetSubsetIndex]):
                        pathB[subsetIndex] = pathB[subsetIndex].union(pathB[offsetSubsetIndex])
                        pathB.pop(offsetSubsetIndex)
                        doBreak = True
                        break
                if doBreak:
                    break

            print("New B: ")
            print(pathB)
            print(knownPointsB)
            print(edgesB)

            if len(list(knownPointsB)) == n:
                print("Old result: " + str(result))
                print(edgesB)
                result += len(edgesB) # add remaining edges
                print("New result: " + str(result))
                break
            elif len(edgesB) != 0 or not addedNew or len(list(knownPointsB)) == n:
                return -1

        return result
