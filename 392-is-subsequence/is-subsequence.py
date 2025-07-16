class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        for i in range(len(s)):
            while j<len(t):
                if t[j] == s[i]:
                    j+=1
                    break
                j += 1
            else:
                return False
        return True
            


            

        

