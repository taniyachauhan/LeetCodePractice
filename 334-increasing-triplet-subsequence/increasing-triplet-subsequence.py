class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # i = 0
        # j=i+1
        # k=j+1
        # while i<len(nums)-2:   
        #     while j <len(nums)-1:
        #         while k < len(nums):
        #             if nums[i]<nums[j] and nums[j]<nums[k]:
        #                 return True
        #             else:
        #                 k += 1
        #         j += 1
        #         k = j + 1
        #     i += 1
        #     j = i + 1
        #     k = j + 1
        # return False

        # O(N) Complexity
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False

            
        