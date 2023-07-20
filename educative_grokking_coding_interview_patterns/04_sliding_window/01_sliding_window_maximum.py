from collections import deque

def find_max_sliding_window(nums, window_size):
    result = []

    window = deque()
    for i, n in enumerate(nums):
        # rm left n if it's outside of window
        if window and window[0] <= i - window_size:
            window.popleft()
        
        # rm nums less than current num
        while window and nums[window[-1]] <= n:
            window.pop()
        window.append(i)
        
        # add result if we have full window
        if i >= window_size - 1:
            result.append(nums[window[0]])

    return result