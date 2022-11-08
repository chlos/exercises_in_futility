#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countProcessors' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY data as parameter.

# [{30, 75}] // 1
# [{30, 75}, {0, 50}] // 2
# [{30, 75}, {100, 150}] // 1
# [{0, 2}, {0, 2}, {2, 4}, {2, 4}, {4, 6}, {4, 6}, {6, 8}, {6, 8}] // 2
# [{0, 10}, {10, 20} {20, 30} {30, 40}] // 1


class Item():
    def __init__(self, ts, typ):
        self.ts = ts
        self.typ = typ
        
    def __repr__(self):
        return "{} - {}".format(self.ts, self.typ)

# O(N*logN)
# O(N)
def countProcessors(data):
    items = []
    for ts_start, ts_end in data:
        items.append(Item(ts_start, "1start"))
        items.append(Item(ts_end, "0end"))
    items = sorted(items, key=lambda item: (item.ts, item.typ))
    print(items)
    
    curr_cpus = 0
    max_cpus = 0
    for item in items:
        if item.typ == "1start":
            curr_cpus += 1
        else:
            curr_cpus -= 1
        if curr_cpus > max_cpus:
            max_cpus = curr_cpus
            
    return max_cpus


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    data_rows = int(input().strip())
    data_columns = int(input().strip())

    data = []

    for _ in range(data_rows):
        data.append(list(map(int, input().rstrip().split())))

    result = countProcessors(data)
    
    # tasks number: 0, 1, >1
    # intersect: yes, no
    # start time 1 eq start time 2: yes, no
    # end time 1 eq end time 2: yes, no
    # 
    # result = countProcessors([[30, 75], [30, 80]])
    # assert result == 2
    # result = countProcessors([[30, 75], [35, 75]])
    # assert result == 2
    # result = countProcessors([[30, 75], [30, 75]])
    # assert result == 2
    # result = countProcessors([[30, 75], [75, 100]])
    # assert result == 1
    # result = countProcessors([[30, 75], [40, 90]])
    # assert result == 2
    # result = countProcessors([[30, 75], [40, 70]])
    # assert result == 2

    fptr.write(str(result) + '\n')

    fptr.close()