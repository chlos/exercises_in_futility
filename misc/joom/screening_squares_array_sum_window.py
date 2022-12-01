# сортированный массив квардратов
# [1, 2, 3] -> [1, 4, 9]
# [-6, -5, 1, 2, 3] -> [36, 25, 1, 4, 9]
# [-5, -2, -1, 3, 4, 5]  --- [25, 4, 1]
# 1, 9!!!, 4, 16, 25, 25
# 
def get_sqr_array(nums):
    result = []
    negative_squares = []
    for n in nums:
        sq = n ** 2
        if n < 0:
            negative_squares.append(sq)
        else:
            while negative_squares and negative_squares[-1] < sq:
                result.append(negative_squares.pop())
            result.append(sq) # fixme
    
    while negative_squares:
        result.append(negative_squares.pop())
    
    return result
    
###########################################

# сумма в окне
# [1, 2, 3, |4, 5|] 2 -> [3, 5, 7, 9]
#            3  4
def get_sums(nums, window_size):
    sums = []
    
    curr_sum = 0
    for i in range(window_size):
        curr_sum += nums[i]
    sums.append(curr_sum)
    
    for i in range(1, len(nums) - window_size):
        curr_sum -= nums[i - 1]
        curr_sum += num[i + window_size - 1]
        sums.append(curr_sum)
        
    return sums
    
############################################