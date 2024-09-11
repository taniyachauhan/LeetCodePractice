class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = {}
        for i in s:
            if i in frequencies:
                frequencies[i] += 1
            else:
                frequencies[i] = 1
        
        seen = set()
        deletions = 0
        
        for freq in frequencies.values():
            while freq in seen:
                freq -= 1
                deletions += 1
            if freq > 0:
                seen.add(freq)
        
        return deletions
        