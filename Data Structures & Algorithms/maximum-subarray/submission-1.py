class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = global_max = nums[0]

        for i in range(1,len(nums)):
            curr = nums[i]
            curr_max = max(nums[i],curr_max+curr)
            global_max = max(global_max,curr_max)
        
        return global_max
        