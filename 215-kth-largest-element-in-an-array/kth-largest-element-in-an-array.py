class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

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
            nums[p], pivot = pivot, nums[p]

            if p < k:
                return quickSelect(l,p-1)
            elif p > k:
                return quickSelect(p+1, r)
            else:
                return nums[p]
        return quickSelect(0, len(nums)-1)


        