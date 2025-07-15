class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        result=[]
        while l<=r:
            if s[l].isalnum() and s[r].isalnum() and s[l].lower()==s[r].lower():
                l += 1
                r -= 1
            elif s[l].isalnum() and s[r].isalnum() and s[l].lower()!=s[r].lower():
                return False
            elif not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
        if l>=r:
            return True
        return False


        

