class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dict=defaultdict(int)
        for i in words1:
            for j in words2:
                if i==j:
                    dict[i]+=1
        return len([k for k in dict.keys() if dict[k]==1])
