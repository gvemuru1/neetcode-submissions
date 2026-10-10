class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapu = {}
        for i, val in enumerate(nums):
            mapu[val] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mapu and i != mapu.get(diff):
                return [i, mapu.get(diff)]