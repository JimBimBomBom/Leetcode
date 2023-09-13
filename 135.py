class Solution:
    def candy(self, ratings: List[int]) -> int:
        r_count = len(ratings)
        result = r_count
        peak_candy = dict()
        count = 0
        index = 0
        while(index < r_count - 1):
            if ratings[index] < ratings[index + 1]:
                count += 1
            else:
                if count:
                    result += sum([x for x in range(1, count+1)])
                    peak_candy[index] = count
                count = 0
            index += 1
        result += sum([x for x in range(1, count+1)])
        count = 0
        while index > 0:
            if ratings[index] < ratings[index - 1]:
                count += 1
            else:
                if count:
                    peak_value = peak_candy.get(index, 0)
                    if peak_value < count:
                        result += sum([x for x in range(1, count)])
                        result += count - peak_value
                    else:
                        result += sum([x for x in range(1, count)])
                count = 0
            index -= 1
        result += sum([x for x in range(1, count+1)])
        return result     