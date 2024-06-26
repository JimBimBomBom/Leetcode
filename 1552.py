class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        valid_positions = set(position)

        start = position[0]
        end = position[-1]
        interval = int((end - start) // (m - 1))

        curr_interval = interval
        while curr_interval > 1:
            print("Starting: ", start)
            current = start
            steps_remaining = m - 1

            print("Interval: ", curr_interval)
            while steps_remaining > 0:
                if (current + curr_interval) in valid_positions:
                    current += curr_interval
                    print("Exact match found!")
                    print("Current: ", current)
                    steps_remaining -= 1
                else:
                    for i in range(curr_interval, interval):
                        if (current + curr_interval + i) in valid_positions:
                            current += curr_interval + i
                            print("Closest match found!")
                            print("Current: ", current)
                            steps_remaining -= 1
                            break
                        else:
                            curr_interval -= 1
                            break
            
            return curr_interval
        