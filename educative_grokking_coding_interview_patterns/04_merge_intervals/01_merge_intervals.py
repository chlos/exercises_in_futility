class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed

    # set the flag for closed/open
    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
                "(" + str(self.start) + ", " + str(self.end) + ")"


def merge_intervals(v):
    result = []
    for curr_inter in v:
        if not result:
            result.append(curr_inter)
            continue
            
        prev_inter = result[-1]
        if curr_inter.start <= prev_inter.end:
            result[-1].end = max(prev_inter.end, curr_inter.end)
        else:
            result.append(curr_inter)

    return result