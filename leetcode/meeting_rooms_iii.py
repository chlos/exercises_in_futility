# nice diagrams: https://leetcode.com/problems/meeting-rooms-iii/solutions/2527317/python-3-explanation-with-pictures-priority-queue/
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms_count = collections.defaultdict(int)

        # sort intervals by start times
        meetings.sort()
        print(meetings)

        # min heap for (end_i, room_number)
        pq_used = []
        # min heap for free room numbers
        pq_free = [nr for nr in range(n)]

        for curr_start, curr_end in meetings:
            # process rooms that are already free
            while pq_used and pq_used[0][0] <= curr_start:
                end_i, room_n = heapq.heappop(pq_used)
                heapq.heappush(pq_free, room_n)

            if pq_free:
                # just taka a free room
                room = heapq.heappop(pq_free)
                end = curr_end
            else:
                # wait for the used room with nearest ending time to free
                # start the new meeting when nearest ending ends
                prev_end, room = heapq.heappop(pq_used)
                duration = curr_end - curr_start
                end = prev_end + duration

            # assign a room
            heapq.heappush(pq_used, (end, room))
            rooms_count[room] += 1

        # most popular room
        max_room, max_count = None, 0
        for room, count in rooms_count.items():
            if count > max_count:
                max_room, max_count = room, count
        return max_room