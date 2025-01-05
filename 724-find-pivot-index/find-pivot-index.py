class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        print(prefix)

        for i in range(1,len(nums)):
            prefix[i]= prefix[i-1]+nums[i-1]
        print(prefix)
        for i in range(len(nums)-2,-1,-1):
            suffix[i]= suffix[i+1]+nums[i+1]
        print(suffix)

        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i
        return -1


        