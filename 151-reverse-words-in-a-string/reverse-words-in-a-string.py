class Solution:
    def reverseWords(self, s: str) -> str:
        # s=s.strip()
        # ozzo=[]
        # temp=""
        
        # i=0
        # while i<len(s):
        #     if s[i] != " ":
        #         temp += s[i]
        #         i+=1

        #     elif s[i] == " ":
        #         ozzo.append(temp)
        #         ozzo.append(s[i])
        #         temp=""
        #         while s[i]==" ":
        #             i+=1
            
        #     if i == len(s):
        #         ozzo.append(temp)
        # return "".join(ozzo[::-1])

        result = []
        s = s.strip()
        temp = []
        i = 0
        while i < len(s):
            if s[i] == " " and s[i+1] != " ":
                result.append("".join(temp))
                temp = []
            elif s[i] == " ":
                pass
            elif i == len(s)-1:
                temp.append(s[i])
                result.append("".join(temp))
            else:
                temp.append(s[i])
            i += 1

        return " ".join(result[::-1])

                








        