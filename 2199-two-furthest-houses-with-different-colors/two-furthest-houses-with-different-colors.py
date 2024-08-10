class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # max_dist = float("-inf")
        # l = 0
        # n = len(colors)
        
        # while l < n - 1:
        #     r = n - 1
        #     while r > l and colors[l] == colors[r]:
        #         r -= 1
        #     #if r > l:
        #     max_dist = max(max_dist, r - l)
        #     l += 1
        # return max_dist

        # O(n) complexity solution
        
        max_dist = 0
        for i, color in enumerate (colors):
            if color != colors[0]:
                max_dist = max(i, max_dist)
            if color != colors[-1]:
                max_dist = max(len(colors)-1-i, max_dist)
        return max_dist



        