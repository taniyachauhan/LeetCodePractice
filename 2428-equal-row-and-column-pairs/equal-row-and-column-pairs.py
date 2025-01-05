class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result = []
        i = 0
        n = len(grid)

        while i < n:
            j = i
            temp = []
            for j in range(n):
                temp.append(grid[j][i])
                j += 1
            result.append(temp)
            i += 1
        print(result)
        counter = 0
        for i in range(n):
            for j in range(n):
                if grid[i] == result[j]:
                    counter += 1
        return counter

        

        