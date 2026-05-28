
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mymap={}
        for num in nums:
            if num in mymap:
                return True
            mymap[num] = 1
        return False    
     
         