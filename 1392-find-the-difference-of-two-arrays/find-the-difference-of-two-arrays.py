class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = []

        dict1 = {}
        dict2 = {}

        for i in nums1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        for i in nums2:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
        temp = []
        for i in dict1.keys():
            if i not in dict2.keys():
                temp.append(i)
        result.append(temp)
        temp =[]

        for i in dict2.keys():
           if i not in dict1.keys():
                temp.append(i)
        result.append(temp)
        return result


        