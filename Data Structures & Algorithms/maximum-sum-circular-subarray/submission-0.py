class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        glob_max = nums[0]
        curr_max = nums[0]
        glob_min = nums[0]
        curr_min = nums[0]
        min_lin = nums[0]
        summ = sum(nums)

        for i in range(1,n):
            curr = nums[i]
            curr_max = max(curr_max+curr,curr)
            glob_max = max(glob_max,curr_max)

            curr_min = min(curr_min+curr,curr)
            glob_min = min(glob_min,curr_min)

        if summ == glob_min:
            return glob_max 
        else:
            return max(glob_max,summ-glob_min)           
            
        