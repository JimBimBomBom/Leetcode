class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [[0, 0, 0] for _ in range(n)]
        for i in range(n):
            rooms[i][2] = i

        meetings.sort(key=lambda x: x[0])

        time = 0
        while meetings:
            meeting = meetings.pop(0)
            meetingLen = meeting[1] - meeting[0]
            time = meeting[0]

            print(meeting)
            rooms.sort(key=lambda x: (x[0] > time, x[2])) #  x[0] > time results in a boolean, where false comes before true
            print("ROOMS")
            print(rooms)
            if time < rooms[0][0]:
                rooms.sort(key=lambda x: (x[0], x[2]))
                print(rooms)
            # rooms[0] = [rooms[0][0] + meeting[1], rooms[0][1] + 1, rooms[0][2]] # TODO maybe add -1 to the meeting[1]?
            rooms[0] = [max(rooms[0][0] + meetingLen, meeting[1]), rooms[0][1] + 1, rooms[0][2]]
            print(rooms)
        
        rooms.sort(key=lambda x: (-x[1], x[2]))

        return rooms[0][2]
