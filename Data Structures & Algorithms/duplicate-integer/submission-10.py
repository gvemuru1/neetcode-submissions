class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapu = len(set(nums))
        if len(nums) == mapu:
            return False
        else:
            return True
        