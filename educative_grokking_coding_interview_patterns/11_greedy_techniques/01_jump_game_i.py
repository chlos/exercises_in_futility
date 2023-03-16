def jump_game(nums):
    curr_target = len(nums) - 1
    for i in reversed(range(len(nums))):
        if curr_target - i <= nums[i]:
            curr_target = i

    return curr_target == 0