class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        l = 0
        r = len(nums)-1
        counter = 0

        while l<r:
            sum = nums[l]+nums[r]

            if sum == k:
                counter += 1
                l += 1
                r -= 1
            elif sum < k:
                l += 1
            elif sum > k:
                r -= 1
        return counter

            

        