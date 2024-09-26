class MyCalendar:
    schedule : List[Tuple[int, int]]

    def __init__(self):
        self.schedule = list()

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.schedule)):
            if start >= self.schedule[i][0]:
                if start >= self.schedule[i][1]:
                    continue
                return False
            else:
                if end <= self.schedule[i][0]:
                    self.schedule.insert(i, (start, end))
                    return True
                return False
        self.schedule.append((start, end))
        return True
