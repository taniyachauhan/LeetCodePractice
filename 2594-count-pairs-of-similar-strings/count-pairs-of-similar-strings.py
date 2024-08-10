class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if set(words[i]) == set(words[j]):
                    count+=1
        return count

        # SECOND ATTEMPT USING HASH MAP, SETS AND PAIRS FROM A SET
        # temp_dict = {}
        # for word in words:
        #     temp = "".join(sorted(set(word)))
        #     if temp not in temp_dict:
        #         temp_dict[temp] = 1
        #     else:
        #         temp_dict[temp] += 1
        # count = 0
        # for value in temp_dict.values():
        #     count += value * (value-1)/2
        # return int(count)
