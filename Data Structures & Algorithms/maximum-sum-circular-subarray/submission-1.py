class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        curmin,curmax = nums[0],nums[0]
        globmax,globmin = nums[0],nums[0]
        total = nums[0]

        for i in range(1,n):
            curr = nums[i]
            total+=curr
            curmin = min(curmin+curr,curr)
            curmax = max(curmax+curr,curr)
            globmax=max(globmax,curmax)
            globmin=min(globmin,curmin)

        if total == globmin:
            return globmax 
        else:
            return max(total -globmin,globmax)        