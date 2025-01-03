class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # i=0
        # merged=[]
        # while i<max(len(word1), len(word2)):
        #     if i<len(word1) and i<len(word2):
        #         merged.append(word1[i])
        #         merged.append(word2[i])
        #     elif i<len(word1) and i>=len(word2):
        #         merged.extend(word1[i:len(word1)])
        #         break
        #     elif i<len(word2) and i>=len(word1):
        #         merged.extend(word2[i:len(word2)])
        #         break
        #     i+=1
        # return "".join(merged)

        # SECOND ATTEMPT
        # matched = []
        # for (i, j) in itertools.zip_longest(word1, word2, fillvalue=""):
        #     matched.append(i)
        #     matched.append(j)
        
        # return "".join(matched)

        # THIRD ATTEMPT
        i = 0
        n = min(len(word1),len(word2))
        result=""

        while i<n:
            result += word1[i]
            result += word2[i]
            i += 1
        if i < len(word1):
            result += word1[i:]
        else:
            result += word2[i:]
        return result

