class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals=[]
        intervals.sort()

        for i in intervals:
            if len(merged_intervals) == 0:
                merged_intervals.append(i)
                continue
            if self.overlap(merged_intervals[-1], i):
                merged_intervals[-1]=[merged_intervals[-1][0], max(merged_intervals[-1][1], i[1])]
            else:
                merged_intervals.append(i)
        return merged_intervals


    def overlap(self, temp, a):
        if a[0] <= temp[1]:
            return True
        return False


