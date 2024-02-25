def handleUncertainCases(groupMeetings, secretKnowers):
    secretKnowersLeft = list(secretKnowers.copy())
    for knower in secretKnowersLeft:
        if knower in groupMeetings.keys():
            for person in groupMeetings[knower]:
                if person not in secretKnowers:
                    secretKnowersLeft.append(person)
                    secretKnowers.add(person)

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secretKnowers = {0, firstPerson}

        groupMeetings = {}
        newTimeDict = {}
        for meeting in sorted(meetings, key=lambda x: x[2]):
            if meeting[2] not in newTimeDict:
                newTimeDict[meeting[2]] = True
                print(groupMeetings)
                if groupMeetings != {}:
                    handleUncertainCases(groupMeetings, secretKnowers)
                    # print(secretKnowers, "After")
                    groupMeetings = {}

            if meeting[0] in secretKnowers or meeting[1] in secretKnowers:
                secretKnowers.add(meeting[1])
                secretKnowers.add(meeting[0])
                continue

            if meeting[0] not in groupMeetings:
                groupMeetings[meeting[0]] = []
            groupMeetings[meeting[0]].append(meeting[1])

            if meeting[1] not in groupMeetings:
                groupMeetings[meeting[1]] = []
            groupMeetings[meeting[1]].append(meeting[0])

        print(groupMeetings)
        handleUncertainCases(groupMeetings, secretKnowers)
        # print(secretKnowers, "After")
        # print("Return")
        return list(secretKnowers)
