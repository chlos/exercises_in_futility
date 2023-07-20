def find_sum_of_three(nums, target):
   nums.sort()

   for i in range(len(nums)):
      low, high = i + 1, len(nums) - 1
      
      while low < high:
         curr_sum = nums[i] + nums[low] + nums[high]
         if curr_sum == target:
            return True
         elif curr_sum < target:
            low += 1
         else:
            high -= 1
   
   return False