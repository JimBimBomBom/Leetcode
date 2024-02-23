class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        statsForCity = [[] for _ in range(n)]

        k += 1 # k stops + 1 to get to destination
        statsForCity[src].append((0, k))
        citiesToSearch = [src]
        while citiesToSearch != []:
            # print(citiesToSearch)
            # print(statsForCity)
            # print("Start")
            currCity = citiesToSearch.pop(0)
            flightsFromCity = [flight for flight in flights if flight[0] == currCity]
            for currPath in statsForCity[currCity]:
                if currPath[1] == 0:
                    continue
                for flight in flightsFromCity:
                    for flightStat in statsForCity[flight[1]]:
                        if flightStat[1] <= currPath[1] -1 and flightStat[0] > currPath[0] + flight[2]:
                            statsForCity[flight[1]].remove(flightStat)

                    if statsForCity[flight[1]] == []:
                        statsForCity[flight[1]].append((currPath[0] + flight[2], currPath[1] - 1))
                        citiesToSearch.append(flight[1])
                    elif max([path[1] for path in statsForCity[flight[1]]]) < currPath[1] - 1:
                        statsForCity[flight[1]].append((currPath[0] + flight[2], currPath[1] - 1))
                        citiesToSearch.append(flight[1])
                    elif min([path[0] for path in statsForCity[flight[1]]]) > currPath[0] + flight[2]:
                        statsForCity[flight[1]].append((currPath[0] + flight[2], currPath[1] - 1))
                        citiesToSearch.append(flight[1])

        if statsForCity[dst] == []:
            return -1
        else:
            return min([path[0] for path in statsForCity[dst]])
