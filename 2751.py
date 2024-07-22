class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        sortedRobots = sorted(zip(positions, healths, directions), key=lambda x: x[0])
        nPos = [x[0] for x in sortedRobots]
        nHea = [x[1] for x in sortedRobots]
        nDir = [x[2] for x in sortedRobots]
        print(nPos, nHea, nDir)
        i = 0
        while True:
            try:
                i = nDir.index('L')
                # print("I: ", i)
                if len(nDir) == 1:
                    break
                if i == 0:
                    for x in range(len(nDir)):
                        if nDir[x] == 'R':
                            nPos = nPos[x:]
                            nDir = nDir[x:]
                            break
                else:
                    RIndex = i - 1
                    index1 = positions.index(nPos[i])
                    index2 = positions.index(nPos[RIndex])
                    if healths[index1] > healths[index2]:
                        health = healths[index1]
                        for x in range(RIndex, 0, -1):
                            if nHea[x] > health:
                                nHea[x] -= 1
                                healths.pop(index1)
                            else:
                                health -= 1
                        while RIndex >= 0 and healths[index1] > healths[index2]:
                            healths[index1] -= 1

                            # print(index2)
                            # print(healths, positions)
                            # healths.pop(index2)
                            healths[index2] = 0
                            positions.pop(index2)

                            nPos.pop(RIndex)
                            nDir.pop(RIndex)

                            RIndex -= 1
                            index2 = positions.index(nPos[RIndex])
                            # print("Start")
                            # print(healths, nPos, nDir)
                            # print(index2, index1)
                            # print("end")
                    elif healths[index1] < healths[index2]:
                        healths.pop(index1)
                        positions.pop(index1)

                        nPos.pop(i)
                        nDir.pop(i)
                        healths[index2] -= 1
                        # print("Start1")
                        # print(healths, nPos, nDir)
                        # print(index2, index1)
                        # print("end")
                    else:
                        # print("Start2")
                        # print(healths, nPos, nDir)
                        # print(index2, index1)
                        healths.pop(index1)
                        positions.pop(index1)
                        nPos.pop(i)
                        nDir.pop(i)

                        healths.pop(index2)
                        positions.pop(index2)
                        nPos.pop(RIndex)
                        nDir.pop(RIndex)
                        # print(healths, nPos, nDir)
                        # print(index2, index1)
                        # print("end")
            except ValueError:
                break

        return healths
