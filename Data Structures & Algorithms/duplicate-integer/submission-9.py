class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapu = set(nums)
        if len(nums) == len(mapu):
            return False
        else:
            return True
        