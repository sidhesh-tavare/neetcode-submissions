class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n-1 
        
        for i in range(goal,-1,-1):
            path = goal - i
            if nums[i]>=path:
                goal = i

        return True if goal==0 else False
              

        