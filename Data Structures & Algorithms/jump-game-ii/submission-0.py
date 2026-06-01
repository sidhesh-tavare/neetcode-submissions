class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        goal = n-1 
        curr_end,farthest,jump =0,0,0
        for i in range(goal):
            farthest = max(farthest,i+nums[i])
            if i==curr_end:
                curr_end=farthest
                jump+=1
        
        return jump
