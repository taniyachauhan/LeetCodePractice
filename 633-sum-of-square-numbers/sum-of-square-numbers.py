class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # l = 0
        # r = c
        # while l <= r:
        #     mid=(l+r)//2
        #     if l**2 + mid**2 == c:
        #         return True             
        #     elif l**2 + mid**2 > c:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return False


        # SECOND ATTEMPT
        
        left = 0
        right = ceil(sqrt(c))

        while left <= right:

            if left* left + right*right ==  c:
                return True
            elif left*left + right*right < c:
                left += 1         
            else:
                right -= 1
        return False





        