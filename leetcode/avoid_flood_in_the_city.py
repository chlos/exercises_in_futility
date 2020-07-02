#!/usr/bin/env python3

import heapq
from collections import defaultdict
from collections import deque
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # lake -> rainy days for this lake
        lake_rain_days = defaultdict(deque)
        # priority heap with lakes to empty at first
        to_empty = []
        # a set of lakes are already full
        is_full = set()
        result = [-1] * len(rains)
        for day, lake in enumerate(rains):
            lake_rain_days[lake].append(day)

        for day, lake in enumerate(rains):
            # it is rainy day
            if lake:
                if lake in is_full:
                    # failed to avoid the flood
                    return []
                is_full.add(lake)
                lake_rain_days[lake].popleft()
                if lake_rain_days[lake]:
                    heapq.heappush(to_empty, lake_rain_days[lake][0])
            # a day to empty some lake
            else:
                if to_empty:
                    nearest_flood_day = heapq.heappop(to_empty)
                    lake_to_empty = rains[nearest_flood_day]
                    result[day] = lake_to_empty
                    is_full.remove(lake_to_empty)
                else:
                    result[day] = 1

        return result


if __name__ == "__main__":
    s = Solution()

    rains = [1, 2, 3, 4]
    res = s.avoidFlood(rains)
    print('\nCheck', rains)
    assert res == [-1, -1, -1, -1]
    print('OK')

    rains = [1, 2, 0, 0, 2, 1]
    res = s.avoidFlood(rains)
    print('\nCheck', rains)
    assert res == [-1, -1, 2, 1, -1, -1]
    print('OK')