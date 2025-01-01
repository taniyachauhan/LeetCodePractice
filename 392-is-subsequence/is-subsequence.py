class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        result = ""
        for letter in s:
            while i<len(t):
                if letter == t[i]:
                    result += t[i]
                    i += 1
                    break
                else:
                    i += 1

        return s == result 
            

        

