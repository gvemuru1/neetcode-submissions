class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ashi={}

        for i in nums:
            if i in ashi:
                return True
            else: 
                ashi[i] = 1
        return False

        