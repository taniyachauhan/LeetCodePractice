class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        steps = 0
        unique = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] <= unique:
                steps += unique - nums[i] + 1
                unique += 1
            else:
                unique = nums[i]
        
        return steps



