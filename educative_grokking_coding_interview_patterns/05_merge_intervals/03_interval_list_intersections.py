from interval import Interval

# Function to find the intersecting points between two intervals
def intervals_intersection(interval_list_a, interval_list_b):
    result = []

    first_i, second_i = 0, 0
    while first_i < len(interval_list_a) and second_i < len(interval_list_b):
        print(first_i, second_i)
        # find the potential intersection start-end
        first_interval, second_interval = interval_list_a[first_i], interval_list_b[second_i]
        possible_intersect_start = max(first_interval.start, second_interval.start)
        possible_intersect_end = min(first_interval.end, second_interval.end)

        # check if it's really intersection
        if possible_intersect_start <= possible_intersect_end:
            result.append(Interval(possible_intersect_start, possible_intersect_end))

        # move to the next interval
        # in list where the curr interval ends earlier
        if first_interval.end < second_interval.end:
            first_i += 1
        else:
            second_i += 1

    return result