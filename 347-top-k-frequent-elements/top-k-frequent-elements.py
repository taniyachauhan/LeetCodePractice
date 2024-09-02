class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_dict = {}
        for i in range(len(nums)) :
            if nums[i] in map_dict:
                map_dict[nums[i]] += 1
            else:
                map_dict[nums[i]] = 1
        map_dict=sorted(map_dict.items(), key=lambda item: item[1])
        return [x[0] for x in map_dict][-k:]

        