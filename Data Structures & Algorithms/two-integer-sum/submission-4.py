class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapu={}

        for i, v in enumerate(nums):
            mapu[v] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mapu and mapu.get(diff) != i:
                return [i, mapu.get(diff)]
        