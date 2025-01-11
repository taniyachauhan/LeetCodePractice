class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)==k:
            return sum(nums)/k

        max_sum = curr_sum = sum(nums[:k])

        for i in range(k,len(nums)):
            curr_sum = curr_sum + nums[i] - nums[i-k]
            max_sum = max(curr_sum, max_sum)
        return max_sum/k
        