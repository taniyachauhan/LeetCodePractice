import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Using binary search to find the min number for which all bananas would be finished before the available hours

        # l = 1
        # r = max(piles)
        # res = r

        # while l<=r:
        #     k = (l+r)//2
        #     hours = 0
        #     for p in piles:
        #         hours += math.ceil(p/k)

        #     if hours <= h:
        #         res= min(res, k)
        #         r = k-1
        #     else: 
        #         l = k+1
        # return res
 
# SECOND ATTEMPT
# Try to create a function for condition and convert the problem into a simple binary search problem

        def condition (self, speed):
            if sum(ceil(pile/speed) for pile in piles) <= h:
                return True
            return False
        # Binary Search Simple Implementation

        l = 1
        r = max(piles)

        while l < r:
            mid = l + (r-l)//2

            if condition(self, mid):
                r = mid
            else:
                l = mid + 1
        return l
        