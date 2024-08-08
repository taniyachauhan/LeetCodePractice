class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # l=[]
        # for i in nums1:
        #     for j in nums2:
        #         if i==j and i not in l:
        #             l.append(i)
        # return l

        # SECOND ATTEMPT
        dict1 = {}
        for i in nums1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        dict2={}
        for i in nums2:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
        
        result=[]
        for key,value in dict1.items():
            if key in dict2:
                result.append(key)
        return result
