import heapq


def tasks(tasks_list):
    tasks_list.sort()

    num_machines = 0
    end_times = []

    for task_start, task_end in tasks_list:
        if end_times and task_start >= end_times[0]:
            # schedule task on the current machine
            heapq.heappop(end_times)
            heapq.heappush(end_times, task_end)
        else:
            # schedule task on the new machine
            heapq.heappush(end_times, task_end)
            num_machines += 1

    return num_machines


tasks1 = [[1,1],[5,5],[8,8],[4,4],[6,6],[10,10],[7,7]]
print(tasks(tasks1))
tasks3 = [[1,7],[8,13],[5,6],[10,14],[6,7]]
print(tasks(tasks3))