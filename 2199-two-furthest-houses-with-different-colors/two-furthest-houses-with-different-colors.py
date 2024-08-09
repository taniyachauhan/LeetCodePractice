class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist = float("-inf")
        l = 0
        n = len(colors)
        
        while l < n - 1:
            r = n - 1
            while r > l and colors[l] == colors[r]:
                r -= 1
            #if r > l:
            max_dist = max(max_dist, r - l)
            l += 1
        
        return max_dist

        