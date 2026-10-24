class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapu = {}
        for i,v in enumerate(nums):
            if v in mapu:
                return True
            mapu[v] =i
        
        return False
        