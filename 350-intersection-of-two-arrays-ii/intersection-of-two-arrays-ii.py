class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # l=[]
        # for i in nums1:
        #     for j in nums2:
        #         if i==j:
        #             l.append(i)
        #             nums2.remove(i)
        #             break
        # return l

        # SECOND ATTEMPT
        dict1 = {}
        for i in nums1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        dict2 = {}
        for i in nums2:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
        min_dic={}
        for key, value in dict1.items():
            if key in dict2 and dict2[key]<value:
                min_dic[key]=dict2[key]
            elif key in dict2 and dict2[key]>=value:
                min_dic[key]=value
        print(min_dic)
        return[key for key, value in min_dic.items() for _ in range(value)]

