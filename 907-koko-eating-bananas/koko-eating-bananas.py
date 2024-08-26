import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Using binary search to find the min number for which all bananas would be finished before the available hours

        l = 1
        r = max(piles)
        res = r

        while l<=r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                res= min(res, k)
                r = k-1
            else: 
                l = k+1
        return res
 

        