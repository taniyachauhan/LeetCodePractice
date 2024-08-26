# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # lst = range(1, n+1)
        # f=0
        # l=len(lst)-1

        # while f <= l:
        #     mid= (f+l)//2
        #     if isBadVersion(lst[mid]) == True and (isBadVersion(lst[mid-1]) == False or mid == 0):
        #         return lst[mid]
        #     elif isBadVersion(lst[mid]) == True:
        #         l = mid-1
        #     elif isBadVersion(lst[mid]) == False:
        #         f = mid+1
        # Second Attempt
        # Factoring in all the possible values 
        l = 1
        r = n

        while l < r :

            mid = l + (r-l)//2

            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l

        



        