class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_dict = {}
        for i in range(len(nums)) :
            if nums[i] in map_dict:
                map_dict[nums[i]] += 1
            else:
                map_dict[nums[i]] = 1
        # map_dict=sorted(map_dict.items(), key=lambda item: item[1])
        # return [x[0] for x in map_dict][-k:]



        keys=[x for x in map_dict.keys()]
        k = len(keys)-k

        def quickSelect(l, r):
            
            pivot = map_dict[keys[r]]
            p = l
            for i in range(l,r):
                if map_dict[keys[i]] <= pivot:
                    keys[i], keys[p] = keys[p], keys[i]
                    p += 1
            keys[p], keys[r] = keys[r], keys[p]

            if p > k:
                return quickSelect(l, p-1)
            elif p < k:
                return quickSelect(p+1, r)
            else:
                return p
        print(keys)
        print(quickSelect(0, len(keys)-1))
        partition = quickSelect(0, len(keys)-1)
        return keys[partition:]
        