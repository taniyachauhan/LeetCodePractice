class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = 0
        altitudes =[0 for x in range(len(gain)+1)]
        print(altitudes)
        for g in range(len(gain)):
            altitudes[g+1] = altitudes[g] + gain[g]
        print(altitudes)
        return max(altitudes)
        