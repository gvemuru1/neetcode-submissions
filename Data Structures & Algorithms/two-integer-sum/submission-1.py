class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapu = {}
        for i, v in enumerate(nums):
            mapu[v] = i
        
        for i in range(len(nums)-1):
            diff = target - nums[i]
            if diff in nums and mapu[diff] != i:
                k = mapu[diff]
                print(k)
                return [i,k]