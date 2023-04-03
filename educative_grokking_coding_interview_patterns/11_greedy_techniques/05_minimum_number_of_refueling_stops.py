class Solution:
    # greedy: max heap / priority queue
    # O(n log n)
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        num_stops = 0
        # we don't any gas station
        if startFuel >= target:
            return num_stops

        stations.append([target, 0])    # add dst as a final "station"

        stations_max_heap = []  # max heap is emulated with min heap and negative values
        prev_position, curr_position = 0, 0
        curr_fuel = startFuel
        for curr_position, curr_station_fuel in stations:
            curr_fuel -= (curr_position - prev_position)

            # the current station is unreachable; we need to refuel on previous stations
            while stations_max_heap and curr_fuel < 0:
                curr_fuel += -heapq.heappop(stations_max_heap)
                num_stops += 1

            # still not enough fuel
            if curr_fuel < 0:
                return -1

            # store curr station data for the future refuels
            prev_position = curr_position
            heapq.heappush(stations_max_heap, -curr_station_fuel)

        return num_stops