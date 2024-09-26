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
        # You sort it in decreasing order and return the kth largest one (Don't have to worry about the duplicates because they don't want kth distinct)
        nums.sort(reverse = True)
        return nums[k-1]

        # Without sorting solution (Using quick select)
        def quickSelect(l,r):
            pivot = nums[r]
            p = l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
                nums[i], pivot = pivot, nums[i]

            if p < k:
                return quickSelect(l,p+1)
            elif p > k:
                return quickSelect(p+1, r)
            else:
                return nums[p]
        return quickSelect(0, len(nums)-1)


        