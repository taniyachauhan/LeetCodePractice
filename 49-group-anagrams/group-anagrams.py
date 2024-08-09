# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         n=len(strs)
#         used=[]
#         lst=[]
#         i=0
#         j=i+1
#         while i < n:
#             temp=[]
#             if i in used:
#                 i+=1
#             else:
#                 temp.append(strs[i])
#                 while i+1<j and j<n:
#                     if j in used:
#                         j+=1
#                     elif j not in used and sorted(strs[i])==sorted(strs[j]):
#                         temp.append(strs[j])
#                         used.append(i)
#                         used.append(j)
#                         j+=1
#                     else:
#                         j+=1
#                 i+=1
#                 lst.append(temp)
#         print(lst)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams = {}
        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        #     if sorted_word in anagrams:
        #         anagrams[sorted_word].append(word)
        #     else:
        #         anagrams[sorted_word] = [word]
        
        # return list(anagrams.values())







        # SECOND ATTEMPT
        result = {}
        sorted_strs = ["".join(sorted(i)) for i in strs]
        print(sorted_strs)
        print(strs)

        for i in range(len(sorted_strs)):
            if sorted_strs[i] not in result:
                result[sorted_strs[i]] = [strs[i]]
            else:
                result[sorted_strs[i]].append(strs[i])
        return (list(result.values()))
            


