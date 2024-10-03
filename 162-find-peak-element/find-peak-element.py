class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Compare middle element with its next neighbor
            if nums[mid] > nums[mid + 1]:
                # Peak lies to the left, including mid
                right = mid
            else:
                # Peak lies to the right
                left = mid + 1

        return left
        
