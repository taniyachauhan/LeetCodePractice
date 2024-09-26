class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # k = len(nums) - k

        # # If we use select sort then average time complexity would be better
        
        # def select_sort(l,r):
        #     pivot, p = nums[len(nums)-1], 0
        #     for i in range(len(nums)):
        #         if nums[i] <= pivot:
        #             nums[i], p = p, nums[i]
        #             p += 1
        #         else:
        #             continue
        #         nums[p], pivot = pivot, nums[p]
        # if p == k:
        #     return nums[p]
        # elif k > p:
        #     return select_sort(p,len(nums)-1)
        # else:
        #     return select_sort(0,p+1)
        # return select_sort(0, len(nums)-1)

        # BRUTE FORCE METHOD
        nums.sort(reverse=True)
        print(nums)
        return nums[k-1]

        