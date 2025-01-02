class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        i = 0
        j = len(word)-1

        while i <=j:
            if word[i] in ('a','e','i','o','u','A','E','I','O','U'):
                while word[j] not in ('a','e','i','o','u','A','E','I','O','U'):
                    j -= 1
                word[i],word[j] = word[j],word[i]
                j -= 1
                i += 1
            else:
                i += 1
        return "".join(word)



        