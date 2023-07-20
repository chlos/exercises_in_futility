from interval import *

def insert_interval(existing_intervals, new_interval):
  result = []

  # add intervals starting before the new one
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