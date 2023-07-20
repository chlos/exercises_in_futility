# https://leetcode.com/problems/exclusive-time-of-functions/solutions/497890/easy-to-understand-python-solution/
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []

        for entry in logs:
            func_id, event_type, event_time = entry.split(":")

            if event_type == "start":
                stack.append([func_id, event_time])

            elif event_type == "end":
                func_id, start_time = stack.pop()
                time_spent = int(event_time) - int(start_time) + 1
                result[int(func_id)] += time_spent

                # decrement time of the next function in the stack to make it exclusive
                if stack:
                    next_func_id, _ = stack[-1]
                    result[int(next_func_id)] -= time_spent

        return result
