START = 0
END = 1


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []

        first_i, second_i = 0, 0
        while first_i < len(firstList) and second_i < len(secondList):
            # find the potential intersection start-end
            first_interval, second_interval = firstList[first_i], secondList[second_i]
            possible_intersect_start = max(first_interval[START], second_interval[START])
            possible_intersect_end = min(first_interval[END], second_interval[END])

            # check if it's really intersection
            if possible_intersect_start <= possible_intersect_end:
                result.append([possible_intersect_start, possible_intersect_end])

            # move to the next interval
            # in list where the curr interval ends earlier
            if first_interval[END] < second_interval[END]:
                first_i += 1
            else:
                second_i += 1

        return result