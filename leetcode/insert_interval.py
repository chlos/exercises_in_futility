START = 0
END = 1

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        result = []
        merged_interval = [newInterval[START], newInterval[END]]

        for interval in intervals:
            if merged_interval is not None and merged_interval[END] < interval[START]:
                result.append(merged_interval)
                merged_interval = None

            if interval[START] < newInterval[START]:
                # no overlapping
                if interval[END] < newInterval[START]:
                    result.append(interval)
                # intersection from the left
                elif newInterval[START] <= interval[END] <= newInterval[END]:
                    merged_interval[START] = interval[START]
                # new interval is inside the current one
                elif newInterval[END] <= interval[END]:
                    result.append(interval)
                    merged_interval = None
            elif newInterval[START] <= interval[START] <= newInterval[END]:
                print("newInterval[START] <= interval[START] <= newInterval[END]")
                # current interval is inside the new one
                if interval[END] <= newInterval[END]:
                    continue
                # intersection from the right
                elif newInterval[END] < interval[END]:
                    merged_interval[END] = interval[END]
                    result.append(merged_interval)
                    merged_interval = None
                    continue
            # no overlapping
            elif newInterval[END] < interval[START]:
                result.append(interval)

        if merged_interval is not None:
            result.append(merged_interval)

        return result


# more concise
def insert_interval(existing_intervals, new_interval):
  result = []

  # add intervals STARTING before the new one
  i = 0
  for curr_inter in existing_intervals:
    if curr_inter.start < new_interval.start:
      result.append(curr_inter)
    else:
      break
    i += 1

  # add and merge the new interval
  prev_inter = None
  if result:
    prev_inter = result[-1]
  if prev_inter and prev_inter.end >= new_interval.start:
    result[-1].end = max(prev_inter.end, new_interval.end)
  else:
    result.append(new_interval)

    
  # add remaining intervals and merge with a new one if needed
  while i < len(existing_intervals):
    curr_inter = existing_intervals[i]
    prev_inter = result[-1]
    if curr_inter.start <= prev_inter.end:
      result[-1].end = max(curr_inter.end, prev_inter.end)
    else:
      result.append(curr_inter)
    i += 1

  return result