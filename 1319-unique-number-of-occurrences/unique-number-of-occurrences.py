class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1 = {}

        for i in arr:
            if i not in dict1.keys():
                dict1[i] = 1
            else:
                dict1[i] += 1

        dict2={}
        for i in dict1.values():
            if i in dict2.keys():
                dict2[i] += 1
                return False
            else:
                dict2[i] = 1
        return True
        