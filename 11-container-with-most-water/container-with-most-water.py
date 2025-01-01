class Solution:
    def maxArea(self, height: List[int]) -> int:
        # #Solving it with brute force and O(n2) time complexity
        # diff = float("-inf")
        # n=len(height)
        # i=0
        # j=n-1
        # while j>i:
        #     while j>i:
        #         if (j-i)*(min(height[i],height[j])) > diff:
        #             diff = (j-i)*min(height[i],height[j])
        #         j-=1
        #     i+=1
        #     j=n-1
        # return diff


        # SECOND ATTEMPT

        i = 0
        j = len(height)-1
        max_area = float("-inf")
        

        while i<j:
            if (j-i) * min(height[i], height[j]) > max_area:
                max_area = (j-i) * min(height[i], height[j])
            if height[i] <= height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
        return max_area