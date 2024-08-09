class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # dict1=defaultdict(int)
        # for i in range(len(words[0])):
        #     if words[0][i] not in dict1:
        #         dict1[words[0][i]]=1
        #     else:
        #         dict1[words[0][i]]+=1
        # for i in range(1, len(words)):
        #     dict2=defaultdict(int)
        #     for j in words[i]:
        #         if j not in dict2:
        #             dict2[j]=1
        #         else:
        #             dict2[j]+=1
        #     for c in list(string.ascii_lowercase):
        #         dict1[c] = min(dict1[c],dict2[c])
        # # dict1=dict(dict1)
        # # print(dict1)
        # return [k for k,v in dict1.items() for _ in range(v)]

        # SECOND ATTEMPT
        temp =[]
        for word in words:
            dictionary = dict.fromkeys(string.ascii_lowercase, 0)
            for i in range(len(word)):
                dictionary[word[i]] += 1
            temp.append(dictionary)

        min_dic={}
        for dic in temp:
            for k,v in dic.items():
                if k not in min_dic or v < min_dic[k]:
                    min_dic[k]=v
        return [key for key, value in min_dic.items() for num in range(value)]





            



