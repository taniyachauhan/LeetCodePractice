@cache
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]!=1:
                return i
        if nums[0]==0:
            return nums[len(nums)-1]+1
        if nums[0]!=0:
            return 0
        