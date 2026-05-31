class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for _,vals in count.items():
            if vals>=2:
                return True
        return False
    