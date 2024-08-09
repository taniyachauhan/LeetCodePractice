import collections
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        temp_list = []
        for i in nums:
            temp_list += i
        return sorted([key for key, value in collections.Counter(temp_list).items() if value == len(nums)])
        