class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        dict1 = {}
        for i in arr1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        dict2 = {}
        for i in arr2:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
        dict3={}
        for i in arr3:
            if i in dict3:
                dict3[i] += 1
            else:
                dict3[i] = 1
        temp = []
        temp.append(dict1)
        temp.append(dict2)
        temp.append(dict3)

        main_dic={}
        for dic in temp:
            for k,v in dic.items():
                if k not in main_dic :
                    main_dic[k] = v
                else:
                    main_dic[k] += v
        print(main_dic)
        return [key for key, value in main_dic.items() if value >2]
        
